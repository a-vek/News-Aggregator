from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Profile, Category


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CategorySelectForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['category']

# class CategoryForm(ModelForm):


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'category']
#     class Meta:
#         model = Category
#         fields = ['cat_name']
#         lables = {
#             'cat_name': 'Enter your categories'
#         }
#         widget = {
#             'cat_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categories'})
#         }

    # category = forms.MultipleChoiceField(

    #     choices=[(agency['id'],

    #               agency['cat_name']) for agency in Category.objects.values('id', 'cat_name')],

    #     widget=forms.SelectMultiple(

    #         attrs={

    #             "class": "select2 form-control select2-multiple",

    #             "multiple": "multiple",

    #             "data-placeholder": "Choose ..."

    #         }

    #     )

    # )


# class CatForm(forms.ModelForm):
#     allCats = forms.ModelChoiceField(queryset=Category.objects.all())
    # class Meta:
    #     model = Categories
    #     fields = ['cat_name']
