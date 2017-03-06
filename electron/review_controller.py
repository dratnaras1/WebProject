from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Review

#CRUD
#REVIEW public
class CreateReview(CreateView):
    model = Review
    fields = ['product', 'review', 'rating', 'user']

class UpdateReviews(UpdateView):
    model = Review
    fields = ['product', 'review', 'rating', 'user']

class DeleteReview(DeleteView):
    model = Review
    fields = ['product', 'review', 'rating', 'user']
