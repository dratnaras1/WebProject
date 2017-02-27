from django.shortcuts import render

# Create your views here.
# hello test

def index(request):
    return render(request,'electron/index.html')