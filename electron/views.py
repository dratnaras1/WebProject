from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserRegistration
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from .models import Product
# Create your views here.
# hello test

def index(request):
    products = Product.objects.order_by('-name')[:4]
    # print(products.length())
    context = {'products': products}
    return render(request,'electron/index.html', context)

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