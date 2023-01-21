from django.urls import path

from . import views

urlpatterns = [
    # ex: /vsgLicense/
    path('', views.index, name='index'),
    # ex: /vsgLicense/5/
    path('<int:customer_id>/', views.detail, name='detail'),
    # ex: /vsgLicense/5/results/
    path('<int:customer_id>/results/', views.results, name='results'),
    # ex: /vsgLicense/5/spinup/
    path('<int:customer_id>/spinup/', views.spinup, name='spinup'),
]
