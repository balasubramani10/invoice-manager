from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        retail_price = request.POST.get('retail_price')
        selling_price = request.POST.get('selling_price')
        stock = request.POST.get('stock')

        if name and retail_price and selling_price:
            Product.objects.create(
                name=name,
                description=description,
                retail_price=retail_price,
                selling_price=selling_price,
                stock=stock if stock else 0
            )
            messages.success(request, "Product added successfully!")
            return redirect('add_product')  
        else:
            messages.error(request, "Please fill all required fields.")

    return render(request, 'add_product.html')


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        retail_price = request.POST.get('retail_price')
        selling_price = request.POST.get('selling_price')
        stock = request.POST.get('stock')

        if name and retail_price and selling_price:
            product.name = name
            product.description = description
            product.retail_price = retail_price
            product.selling_price = selling_price
            product.stock = stock if stock else 0
            product.save()

            messages.success(request, "Product updated successfully!")
            return redirect('view_products')  # Redirect to product list after updating
        else:
            messages.error(request, "Please fill all required fields.")

    return render(request, 'edit_product.html', {'product': product})

def view_products(request):
    search_query = request.GET.get('q', '')
    products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    paginator = Paginator(products, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_products.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect('view_products')  # Update this to your correct view name
