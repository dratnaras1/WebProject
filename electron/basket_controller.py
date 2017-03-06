from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Basket

#CRUD
#Basket
#distinguish between emptying the entire basket and removing a single product from basket...
class AddItemBasket(UpdateView):
    model = Basket
    fields = ['user', 'products']

class EmptyBasket(DeleteView):
    model = Basket
    fields = ['user', 'products']
