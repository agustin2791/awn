from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("new_customer/", views.customer_form, name='new_customer'),
    path("remove_customer/<int:pk>", views.remove_customer, name='remove_customer')
]