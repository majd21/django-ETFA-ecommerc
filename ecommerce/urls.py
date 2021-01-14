from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('products/<int:product_pk>', views.singleProduct, name='singleProduct'),
    path('update_cart/', views.updateCart, name='updateCart'),
    path('cart/', views.cart, name='cart'),
    path('delete_item/', views.deleteItem, name='deleteItem'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_process/', views.checkoutProcess, name='checkoutProcess'),
    path('signup/', views.signup, name='signup'),
    path('signup_process/', views.signupProcess, name='signupProcess'),
]
