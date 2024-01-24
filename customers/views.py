from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.

def index(request):

    customers = Customer.objects.all()

    return render(request, 'customers/index.html', {'customers': customers})

def customer_form(request):
    if request.method == 'POST':
        form = NewCustomer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NewCustomer()    

    return render(request, 'customers/new_customer.html', {'form': form})

def remove_customer(request, *args, **kwargs):
    customer_id = kwargs['pk']
    customer_to_delete = Customer.objects.get(id=customer_id)

    customer_to_delete.delete()

    return redirect('/')