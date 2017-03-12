from django.contrib.auth.models import User
from django import forms

class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(widget=forms.TextInput, required=True)
    last_name = forms.CharField(widget=forms.TextInput, required=True)
    addressline1 = forms.CharField(widget=forms.TextInput, required=True)
    addressline2 = forms.CharField(widget=forms.TextInput, required=False)
    city = forms.CharField(widget=forms.TextInput, required=True)
    phone = forms.CharField(widget=forms.TextInput, required=True)
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=True)

# def saveExtraFields(self, commit=True):
#     addressline1 = self.cleaned_data.get('Address Line 1', None)
#     addressline2 = self.cleaned_data.get('Address Line 2', None)
#     city = self.cleaned_data.get('City', None)
#     phone = self.cleaned_data.get('phone', None)
#
#     return super(UserRegistration, self).save(commit=commit)


    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'addressline1', 'addressline2', 'city', 'phone']
