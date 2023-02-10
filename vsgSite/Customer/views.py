from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Customer, License
from .utils import *
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'Customer/index.html'
    context_object_name = 'latest_customer_list'

    def get_queryset(self):
        return Customer.objects.all()

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    template_name = 'Customer/detail.html'

class ResultsView(LoginRequiredMixin, generic.DetailView):
    model = Customer
    template_name = 'Customer/results.html'

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

