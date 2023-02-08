from django.urls import path

from . import views

app_name = 'Customer'
urlpatterns = [
    # ex: /Customer/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /Customer/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:pk>/spinup/', views.spinup, name='spinup'),
]

