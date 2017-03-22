from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserRegistration
from django.http import HttpResponse
from django.template import loader
from .models import Basket
import basket_controller


from django.shortcuts import render
from .models import Product, Category
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

def show_basket(request):
    basketItemsForUser = basket_controller.getItemsForUser(request)
    totalPriceForUser = basket_controller.getTotalPriceForBasket(request)
    template = loader.get_template('electron/shopping-basket.html')
    context = {
        'allBasketItems': basketItemsForUser,
        'totalPrice': totalPriceForUser,
    }
    return HttpResponse(template.render(context, request))

def delete_item(request):
    basketItemsForUser = basket_controller.getItemsForUser(request)
    totalPriceForUser = basket_controller.getTotalPriceForBasket(request)
    template = loader.get_template('electron/shopping-basket.html')
    quantity = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    context = {
        'quantity': quantity,
        'allBasketItems': basketItemsForUser,
        'totalPrice': totalPriceForUser,
    }
    return HttpResponse(template.render(context, request))

class UserFormView(View):
    form_class = UserRegistration
    template_name = "registration/registration.html"

    #display the blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #submit form data
    def post(self, request):
        template_index = loader.get_template("electron/index.html")
        template_registration = loader.get_template("registration/registration.html")

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #clean/normalised data
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            addressline1 = form.cleaned_data['addressline1']
            addressline2 = form.cleaned_data['addressline2']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            user.set_password(password)
            user.save()

            #returns user objects if details are correct
            user = authenticate(username=username, password=password, first_name=first_name, last_name=last_name,
                                addressline1=addressline1, addressline2=addressline2, city=city, phone=phone,
                                password_confirm=password_confirm)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

                else:
                    # return http resp
                    return HttpResponse(template_index.render("", request))

            else:
                return HttpResponse(template_registration.render("", request))
                # return http resp
        else:
            return HttpResponse(template_registration.render("", request))
            # return http resp

    def clean_password2(self):
        password = self.clean_data.get('password')
        password_confirm = self.clean_data.get('password_confirm')

        if not password_confirm:
            raise forms.ValidationError("You must confirm your password")
        if password != password_confirm:
            raise forms.ValidationError("Your password does not match")

        return render(request, self.template_name, {'form': form})