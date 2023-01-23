from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Customer, Node
import subprocess

def index(request):
    latest_customer_list = Customer.objects.order_by('-add_date')[:5]
    context = {'latest_customer_list': latest_customer_list}
    return render(request, 'Customer/index.html', context)

def detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'Customer/detail.html', {'customer': customer})
def spinup(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.POST:
        subprocess.call('foo.bat', customer_id)
    return render(request, 'Customer/detail.html', {'customer': customer})

def results(request, customer_id):
    response = "You're looking at the nodes for customer %s."
    return HttpResponse(node % customer_id)

