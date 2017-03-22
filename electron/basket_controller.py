from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from .models import Basket, Product

#CRUD
#Basket
#distinguish between emptying the entire basket and removing a single product from basket...
def add_to_basket(request, id):
    product = Product.objects.get(pk=id)
    if Basket.objects.filter(user=request.user, products=product).exists():
        query1 = Basket.objects.get(user=request.user, products=product)
        query1.quantity += 1
        query1.save()
        return redirect('index')
    else:
        query = Basket(user = request.user, products = product, quantity = 1)
        query.save()
        return redirect('index')

def empty_basket(request):
    query = Basket.objects.filter(user = request.user)
    query.delete()
    return redirect('show-basket')

def delete_item(request, id):
    product = Product.objects.get(pk=id)
    #if product has already been added by user then update quanity..
    query = Basket.objects.filter(user = request.user, products = product)
    query.delete()
    return redirect('show-basket')

def getItemsForUser(request):
    currentUser = request.user
    allItemsForUser = Basket.objects.filter(user=currentUser)
    return allItemsForUser

def getTotalPriceForBasket(request):
    currentUser = request.user
    allItemForUser = Basket.objects.filter(user=currentUser)
    total_price = 0
    for item in allItemForUser:
        total_price += (item.products.price * item.quantity)

    return total_price



