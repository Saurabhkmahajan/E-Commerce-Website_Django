from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from store.models.product import Product
from store.models.orders import Order


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        #print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer = Customer(id = customer),
                          product = product,
                          price = product.price,
                          address = address,
                          phone = phone,
                          quantity = cart.get(str(product.id)))

            order.placeoder();
            request.session['cart'] = {}
        return redirect('cart')
