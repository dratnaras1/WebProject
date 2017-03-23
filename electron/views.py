from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserRegistration
from django.http import HttpResponse
from django.template import loader
# from django.contrib.auth.models import User
from .models import Basket
from electron import basket_controller
from electron.forms import ReviewForm
from django.shortcuts import render
from .models import Product, Category, User
from django.views import View
from .forms import UserRegistration, UserLogin
from django.views.generic import View
# Create your views here.
# hello test

def index(request):
    products = Product.objects.order_by('-name')[:4]
    # print(products.length())
    context = {'products': products}
    return render(request,'electron/index.html', context)

def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products,
               'categories' : categories}
    return render(request, 'electron/products.html', context)

def products_category(request, category):
    categories = Category.objects.all()
    category_db = Category.objects.filter(type = category)
    products = Product.objects.filter(category = category_db)
    context = {'products':products,
               'categories' : categories}
    return render(request, 'electron/products_category.html', context)

def individual_product(request, id):
    product = Product.objects.filter(pk=id)
    categories = Category.objects.all()
    context = {'product':product,
               'categories' : categories}
    return render(request, 'electron/individual_product.html', context)


def login_user(request):
    if request.user.is_authenticated:
        # redirect to shop
        return redirect('index')
    else:
        error = None
        if request.method == 'POST':
            form = UserLogin(request.POST)

            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                # check if username exists
                if User.objects.filter(email=email).exists():
                    user = authenticate(username=email, password=password)

                    # if user not null login
                    if user is not None:
                        login(request, user)
                        return redirect('index')
                    else:
                        error = 'Email or password is incorrect'
                else:
                    error = 'Email does not exist'
            else:
                error = 'Form details are invalid.'
        else:
            form = UserLogin()
    context = {'form': form, 'error': error, 'logged_in': False}
    return render(request, 'registration/login.html', context)


@login_required
def show_basket(request):
    basketItemsForUser = basket_controller.getItemsForUser(request)
    totalPriceForUser = basket_controller.getTotalPriceForBasket(request)
    template = loader.get_template('electron/shopping-basket.html')
    quantity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {
        'allBasketItems': basketItemsForUser,
        'totalPrice': totalPriceForUser,
        'quantity': quantity,
    }
    return HttpResponse(template.render(context, request))

def delete_item(request):
    basketItemsForUser = basket_controller.getItemsForUser(request)
    totalPriceForUser = basket_controller.getTotalPriceForBasket(request)
    template = loader.get_template('electron/shopping-basket.html')
    context = {
        'allBasketItems': basketItemsForUser,
        'totalPrice': totalPriceForUser,
    }
    return HttpResponse(template.render(context, request))

class UserFormView(View):
    form_class = UserRegistration
    template_name = "registration/registration.html"

    # display the blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # submit form data
    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # clean/normalised data
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            addressline1 = form.cleaned_data['addressline1']
            addressline2 = form.cleaned_data['addressline2']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            user.set_password(password)

            if password == password_confirm:
                print('Passwords  match')
                user = User.objects.create_user(email=email, password=password, first_name=first_name,
                                                last_name=last_name, addressline1=addressline1,
                                                addressline2=addressline2, city=city, phone=phone)

                login(request, user)
                return redirect('index')

            else:
                return HttpResponse('<h1> password do not match </h1>')

        else:
            return render(request, self.template_name, {'form': form, 'error': 'Error!'})

def review(request, id):
    product = Product.objects.filter(pk=id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            review = form.cleaned_data['review']
            rating = form.cleaned_data['rating']

            r = Review(product=Product(id=id), review=review, rating=rating, user=request.user)
            r.save()

            context = {'form':form}


            return render(request, 'electron/review.html',  context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReviewForm()

    return render(request, 'electron/review.html', {'form':form})