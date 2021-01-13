from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('products/<int:product_pk>', views.singleProduct, name='singleProduct'),
    path('update_cart/', views.updateCart, name='updateCart'),
]