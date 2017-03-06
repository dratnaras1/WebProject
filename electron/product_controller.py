from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product

#CRUD
#PRODUCT private
class CreateProduct(CreateView):
    #image??? and id on top of pk?
    model = Product
    fields = ['name', 'price', 'description', 'image', 'stock', 'category']

class UpdateProduct(UpdateView):
    #image???
    model = Product
    fields = ['name', 'price', 'description', 'image', 'stock', 'category']

class DeleteProduct(CreateView):
    #image???
    model = Product
    fields = ['name', 'price', 'description', 'image', 'stock', 'category']