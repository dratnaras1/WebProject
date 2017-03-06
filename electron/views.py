from django.shortcuts import render
from .models import Product
# Create your views here.
# hello

def index(request):
    products = Product.objects.order_by('-name')[:5]

    # print(products.length())
    print(products)
    context = {'products': products}

    return render(request,'electron/index.html', context)