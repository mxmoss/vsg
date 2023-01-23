from django.urls import path

from . import views

app_name = 'Customer'
urlpatterns = [
    # ex: /Customer/
    path('', views.index, name='index'),
    # ex: /Customer/5/
    path('<int:customer_id>/', views.detail, name='detail'),
    path('<int:customer_id>/results/', views.results, name='results'),
    path('<int:customer_id>/spinup/', views.spinup, name='spinup'),
]

