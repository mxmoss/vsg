from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Customer, Node


def index(request):
    latest_customer_list = Customer.objects.order_by('-add_date')[:5]
    template = loader.get_template('Customer/index.html')
    context = {
        'latest_customer_list': latest_customer_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, customer_id):
    return HttpResponse("You're looking at customer %s." % customer_id)

def results(request, customer_id):
    response = "You're looking at the nodes for customer %s."
    return HttpResponse(node % customer_id)

def spinup(request, customer_id):
    return HttpResponse("You're spinning up a node for customer %s." % customer_id)