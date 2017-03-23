from django.contrib.auth.models import User
from django import forms


class UserRegistration(forms.ModelForm):
    email = forms.CharField(label='Email', widget=forms.TextInput, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password Confirm', widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(label='First Name', widget=forms.TextInput, required=True)
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput, required=True)
    addressline1 = forms.CharField(label='Address Line 1', widget=forms.TextInput, required=True)
    addressline2 = forms.CharField(label='Address Line 2', widget=forms.TextInput, required=False)
    city = forms.CharField(label='City', widget=forms.TextInput, required=True)
    phone = forms.CharField(label='Contact Number', widget=forms.TextInput, required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'first_name', 'last_name', 'addressline1', 'addressline2', 'city', 'phone']


class UserLogin(forms.Form):
    email = forms.CharField(label='Email', widget=forms.TextInput, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class ReviewForm(forms.Form):
    rating = forms.IntegerField()
    review = forms.CharField(widget=forms.Textarea)