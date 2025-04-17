from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from client.models import Client
from django.contrib import messages

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



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


