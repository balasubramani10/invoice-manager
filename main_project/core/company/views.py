from django.shortcuts import render
from product.models import Product
from client.models import Client

def dashboard(request):
    total_clients = Client.objects.count()
    total_products = Product.objects.count()
    last_product = Product.objects.order_by('-id').first()
    last_client = Client.objects.order_by('-id').first()

    context = {
        'total_clients': total_clients,
        'total_products': total_products,
        'last_product': last_product,
        'last_client': last_client,
    }

    return render(request, 'dashboard.html', context)
