from django.forms.models import ModelForm
from django.http.response import HttpResponse
from .models import Category
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CategorySelectForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django import forms
from django.http import HttpResponseRedirect
from news.models import Headline
import requests
from newsapi import NewsApiClient
from django.contrib.auth.models import User

newsapi = NewsApiClient(api_key='0fa3349bf454405e9de70c0b3d92cb38')
news = newsapi.get_sources()


# def add_cat(request):
#     submitted = False
#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/add_cat?submitted=True')
#     else:
#         form = CategoryForm
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'users/add_cat.html', {'form': form, 'submitted': submitted})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('category_list')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def category_list(request):
    if request.method == 'POST':
        c_form = CategorySelectForm(
            request.POST, request.FILES, instance=request.user.profile)
        if c_form.is_valid():
            c_form.save()
            messages.success(
                request, f'Favourite categories have been selected!!')
            return redirect('home')
    else:
        c_form = CategorySelectForm(instance=request.user.profile)
    return render(request, 'users/category.html', {'c_form': c_form})

                                          
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

# def categorypicker(request):
#     # if request.user.is_authenticated:
#     # url = f"https://newsapi.org/v2/top-headlines/sources?apiKey=0fa3349bf454405e9de70c0b3d92cb38"
#     url = f"http://127.0.0.1:8000/newsapi"
#     response = requests.get(url)
#     data = response.json()
#     print(data)
#     categories = []
#     global category_picker
#     category_picker = []
#     for i in data:
#         categories.append(i['category'])
#     print(categories)
#     for i in categories:
#         if i not in category_picker:
#             category_picker.append(i)
#     print(category_picker)
#     # else:
#     #     return "detail:Authentication credentials were not provided."
#     return render(request, 'users/categorypicker.html', {'category_picker': category_picker})
    # abc = "https://newsapi.org/v2/top-headlines/sources?apiKey=0fa3349bf454405e9de70c0b3d92cb38"
    # category_picker = ['general', 'sports', 'business', 'entertainment']
    # for i in range(len(data)):
    #     category_picker.append(data['sources'][i]['category'])
    #     print(category_picker)
# def index(request):
#     results = Category.objects.all()
#     return render(request, 'users/index.html', {'results': results})


# def categorytracker(request):
#     category_selected = request.GET.getlist('category_picker')
#     print(category_selected)
#     articles = {}
#     available_category = category_picker
#     for i in category_selected:
#         if i in available_category:
#             pass
#         else:
#             return HttpResponse("Error")
#     for i in category_selected:
#         url = f"http://127.0.0.1:8000/newsapi/?category={i}"
#         print(url)
#         response = requests.get(url)
#         print(response)
#         data = response.json()
#         print(data)
#         articles.update(data)
#     return render(request, "users/categorytracker.html", {'articles': articles})

    #     print(data)
    #     details = data['articles']
    #     print(articles)
    # for i in details:


# def cate(request):
#     results = Category.objects.all()
#     return render(request, 'users/cate.html', {'results': results})
#     if request.method == 'POST':
#         if request.POST.get('cat_name'):
#             savedata = Category()
#             savedata.cat_name = request.POST.get('cat_name')
#             savedata.save()
#             return render(request, 'users/login.html')
#     return render(request, 'users/cate.html')
