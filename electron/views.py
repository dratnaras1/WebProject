from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.
# hello test

def index(request):
    return render(request,'electron/index.html')

def register(request):
    return render(request,'electron/register.html')