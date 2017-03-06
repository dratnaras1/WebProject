from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserRegistration


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
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #clean/normalised data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user objects if details are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})

