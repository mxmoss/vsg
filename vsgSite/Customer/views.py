from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Customer
from .utils import *
from django.conf import settings
from vsgSite.settings import BASE_DIR, STATIC_URL

def index(request):
    latest_customer_list = Customer.objects.order_by('-add_date')[:5]
    context = {'latest_customer_list': latest_customer_list}
    return render(request, 'Customer/index.html', context)

def detail(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    return render(request, 'Customer/detail.html', {'customer': customer})
def spinup(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer_txt = str(customer_id)
    if request.POST:
        src = os.path.join(settings.STATIC_PATH,'AWSProxy.bat')
        dest = tmpFileName(customer_txt)
        dest.close()
        CopyFile(src, dest.name)
        try:
            exec(dest.name, customer_txt)
        except:
            print("Something went wrong")
        finally:
            os.remove(dest.name)
    return render(request, 'Customer/detail.html', {'customer': customer})

def results(request, customer_id):
    response = "You're looking at the nodes for customer %s."
    return HttpResponse(node % customer_id)

