from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
# Create your views here.


def store(request):
    if request.user.is_authenticated:
        person = request.user
        customer = Customer.objects.filter(user = person)
        
        # order, created = Order.objects.get_or_create(transaction_id = 175243109276, complete = False)
        order, created = Order.objects.get_or_create(customer__in=customer, complete=False)

        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {
            'get_cart_total' : 0,
            'get_cart_items' : 0
        }
        cartItems = order['get_cart_items']


    products = Product.objects.all()

    context = {
        'products' : products,
        'cartItems': cartItems
    }
    return render(request,'shop/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        person = request.user
        customer = Customer.objects.filter(user = person)
        
        # order, created = Order.objects.get_or_create(transaction_id = 175243109276, complete = False)
        order, created = Order.objects.get_or_create(customer__in=customer, complete=False)

        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {
            'get_cart_total' : 0,
            'get_cart_items' : 0,
            'shipping' : False
        }
        cartItems = order['get_cart_items']

    context = {
        'items' : items,
        'order' : order,
        'cartItems': cartItems
    }
    return render(request,'shop/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        person = request.user
        customer = Customer.objects.filter(user = person)
        
        # order, created = Order.objects.get_or_create(transaction_id = 175243109276, complete = False)
        order, created = Order.objects.get_or_create(customer__in=customer, complete=False)

        items = order.orderitem_set.all()
        cartItems = order.get_cart_items


    else:
        items = []
        order = {
            'get_cart_total' : 0,
            'get_cart_items' : 0,
            'shipping': False
        }
        cartItems = order['get_cart_items']

    context = {
        'items' : items,
        'order' : order,
        'cartItems': cartItems
    }
    return render(request,'shop/checkout.html',context)


def updateCart(request):
    
    data = json.loads(request.body)
    print(data)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    print('----------1---------')
    person = request.user
    customer = Customer.objects.filter(user = person)
    print('----------2---------')
    product = Product.objects.get(id=productId)
    print('----------3---------')
    order, created = Order.objects.get_or_create(customer__in=customer, complete=False)
    print('----------4---------')
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	
    if action == 'add':
    	orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
    	orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
    	orderItem.delete()

    return JsonResponse('Item Was Added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)