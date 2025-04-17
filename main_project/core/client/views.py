from .models import Client
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def add_client(request):
    if request.method == 'POST':
        # Handle form submission
        client = Client(
            account_no=request.POST['account_no'],
            name=request.POST['name'],
            local_address=request.POST['local_address'],
            permanent_address=request.POST['permanent_address'],
            tel=request.POST.get('tel', ''),
            mobile=request.POST['mobile'],
            email=request.POST['email'],
            gst=request.POST.get('gst', ''),
            location=request.POST['location'],
            type=request.POST['type'],
            remarks=request.POST.get('remarks', '')
        )
        client.save()
        messages.success(request, 'Client added successfully!')
        return redirect('add_client')  # Redirect to the add client page again (or another page)

    return render(request, 'add_client.html')



@login_required(login_url='login')
def view_clients(request):
    search_query = request.GET.get('search', '')
    clients = Client.objects.all()

    if search_query:
        clients = clients.filter(name__icontains=search_query)

    paginator = Paginator(clients, 10)  # Adjust the number per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'view_clients.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })


@login_required(login_url='login')
def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.account_no = request.POST.get('account_no')
        client.name = request.POST.get('name')
        client.local_address = request.POST.get('local_address')
        client.permanent_address = request.POST.get('permanent_address')
        client.tel = request.POST.get('tel')
        client.mobile = request.POST.get('mobile')
        client.email = request.POST.get('email')
        client.gst = request.POST.get('gst')
        client.location = request.POST.get('location')
        client.type = request.POST.get('type')
        client.remarks = request.POST.get('remarks')
        client.save()
        messages.success(request, "Client updated successfully!")
        return redirect('view_clients')

    return render(request, 'edit_client.html', {'client': client})


@login_required(login_url='login')
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    messages.success(request, "Client deleted successfully!")
    return redirect('view_clients')

