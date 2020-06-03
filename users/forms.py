from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["email","password","nickname","cellphone"]

class UsersInsertForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['image']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["email","password"]

