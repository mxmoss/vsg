from django.urls import path

from . import views

urlpatterns = [
    # ex: /Customer/
    path('', views.index, name='index'),
    # ex: /Customer/5/
    path('<int:customer_id>/', views.detail, name='detail'),
    # ex: /Customer/5/results/
    path('<int:customer_id>/results/', views.results, name='results'),
    # ex: /Customer/5/spinup/
    path('<int:customer_id>/spinup/', views.spinup, name='spinup'),
]
