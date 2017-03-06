from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Order

class CreateOrder(CreateView):
    model = Order
    fields = ['products', 'user', 'total']

class UpdateOrder(UpdateView):
    model  = Order
    fields = ['products', 'user', 'total']

class DeleteOrder(DeleteView):
    model  = Order
    fields = ['products', 'user', 'total']