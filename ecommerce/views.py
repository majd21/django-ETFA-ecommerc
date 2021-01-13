from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer , complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        pass
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'ecommerce/index.html', context)


def products(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer , complete = False)
        cartItems = order.get_cart_item
        items = order.orderitem_set.all()
    else:
        pass
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'ecommerce/products.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer , complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
        cartTotal = order.get_cart_total
    else:
        pass
    products = Product.objects.all()
    context = {'order': order ,'items': items, 'cartItems': cartItems , 'cartTotal': cartTotal}
    return render(request, 'ecommerce/cart.html', context)



def contact(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer  , complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        pass
    context = {'cartItems': cartItems}
    return render(request, 'ecommerce/contact.html', context)


def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer , complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_total
    else:
        pass
    context = {'cartItems': cartItems}
    return render(request, 'ecommerce/about.html', context)


def singleProduct(request, product_pk):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer , complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        pass
    product = get_object_or_404(Product, pk=product_pk)
    products = Product.objects.all()
    context = {'product': product,
               'products': products, 'cartItems': cartItems}
    return render(request, 'ecommerce/single-product.html', context)


def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    quantity = data['quantity']
    print("quantity", quantity)
    print("productId", productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product , quantity = quantity)
    orderItem.save()
    return JsonResponse('item was added', safe=False)

def deleteItem(request):
    data = json.loads(request.body)
    itemId = data['itemId']
    print(itemId)
    item = OrderItem.objects.get(id = itemId)
    item.delete()
    return JsonResponse('item was deleted' , safe=False)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer , complete=False)
    else: 
        pass
    context = {'customer':customer , 'order':order}
    return render(request , 'ecommerce/checkout.html' , context)

def checkoutProcess(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer , complete=False)
    else: 
        pass
    name = data['formData']['name']
    email = data['formData']['email']
    phoneNumber = data['formData']['phone']
    customer , created = Customer.objects.get_or_create(email = email)
    customer.name = name
    customer.phoneNumber = phoneNumber
    customer.save()

    order.transaction_id = transaction_id
    order.complete = True
    order.save()
    
    ShippingAddress.objects.create(
        customer = customer ,
        order = order,
        address = data['formData']['address'],
        city = data['formData']['city'],
        state = data['formData']['state'],
        zipcode = data['formData']['zipcode'],
    )
   
    # order.get_cart_item = 0
    return JsonResponse('Checkout is done' , safe=False)