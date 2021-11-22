from django.forms.models import ModelForm
from django.http.response import HttpResponse
from users.models import Category, Profile
from django import forms
import requests
import json
from django.shortcuts import render, redirect
# from bs4 import BeautifulSoup as BSoup
from news.models import Headline
from newsapi import NewsApiClient
from django.contrib.auth.decorators import login_required


requests.packages.urllib3.disable_warnings()

# newsapi = NewsApiClient(api_key='0fa3349bf454405e9de70c0b3d92cb38')
newsapi = NewsApiClient(api_key='0fa3349bf454405e9de70c0b3d92cb38')

news = newsapi.get_sources()


@login_required
def news_list(request):
    context = None
    categorySelectorUser = Profile.objects.get(user=request.user)
    category_items = categorySelectorUser.category.all()
    # category_items = request.user.profile.category.all()

    print(category_items)
    headline = Headline.objects.filter(category__in=category_items)
    # print(headline)
    context = {
        'object_list': headline,
    }
    print(context)
    return render(request, "news/home.html", context)


def scrape():
    data = news['sources']
    for i in range(len(data)):
        new_headline = Headline()
        new_headline.name = news['sources'][i]['name']
        new_headline.desc = news['sources'][i]['description']
        new_headline.url = news['sources'][i]['url']
        category, created = Category.objects.get_or_create(cat_name=news['sources'][i]['category'])
        new_headline.category = category
        new_headline.save()
    return True
    # new_headline.nid = news['source'][i]['id']
    # new_headline.category = news['sources'][i]['category']
    # new_headline.language = news['sources'][i]['language']
    # new_headline.country = news['sources'][i]['country']
    # new_headline.title = news['articles'][i]['title']
    # new_headline.urlToImage = news['articles'][i]['urlToImage']
    # new_headline.publishedAt = news['articles'][i]['publishedAt']
# def news_list(request):
#     headlines = Headline.objects.all()[::-1]
#     # headlines = Headline.objects.get(pk={})
#     context = {
#         'object_list': headlines,
#     }
#     return render(request, "news/home.html", context)


# enter_news = newsapi.get_top_headlines(
# def starter(request):
#     return render(request, "news/starter.html")


# @login_required
# def news_list(request):
#     user_id = request.users.pk

#     category = UserCategory.objects.get(category=user_id)
#     print(category)
#     context = {
#         'object_list': category,
#     }
#     return render(request, "news/home.html", context)

# @login_required


# def news_list(request):
#     category_selected = request.GET.getlist('category')
#     headline = {}
#     available_category = Category.objects.all()
#     for i in category_selected:
#         if i in available_category:
#             pass
#         else:
#             return HttpResponse("Error")
#     for i in category_selected:
#         url = f"http://127.0.0.1:8000/newsapi/?category={i}"
# #         print(url)
#         response = requests.get(url)
#         data = response.json()
#         headline.update(data)
# #         print(response)
# #         print(data)

#         context = {
#             'object_list': headline,
#         }
#         return render(request, "news/home.html", context)
#     return "fail"
# if request.user.is_authenticated:
#     url = f"http://127.0.0.1:8000/newsapi"
# headline = None
# if 'category' in request.GET:
#     cat_id = request.GET['category']
#     headline = Headline.objects.filter(category=cat_id)
# # for category in request.POST['category']:
# # user_selected_category = UserCategory.objects.filter()
# # selected_category = Headline.objects.all().prefetch_related('category')
# context = {
#     'object_list': headline,
# }
# return render(request, "news/home.html", context)

#     sources='google-news', language='en')

# sources = newsapi.get_sources()
# from newsapi import NewsApiClient

# # Init
# newsapi = NewsApiClient(api_key='0fa3349bf454405e9de70c0b3d92cb38')
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')
# # /v2/top-headlines
# enter_news = newsapi.get_top_headlines(sources='bbc-news,the-verge',
#                                        category='business',
#                                        language='en',
#                                        )


# class CatForm(ModelForm):
#     allCats = forms.ModelChoiceField(queryset=Category.objects.all())

    # r = requests.get(
    #     'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=0fa3349bf454405e9de70c0b3d92cb38')
    # data = json.loads(r.content)
    # a = data['articles']

    # content = session.get(url, verify=False).content
    # soup = BSoup(content, "html.parser")
    # News = soup.find_all('div', {"class": "curation-module__item"})
    # for artcile in News:
    #     main = artcile.find_all('a')[0]
    #     link = main['href']
    #     image_src = str(main.find('img')['srcset']).split(" ")[-4]
    #     title = main['title']
    #     new_headline = Headline()
    #     new_headline.title = title
    #     new_headline.url = link
    #     new_headline.image = image_src
    #     new_headline.save()
    # return redirect("../")

# news = newsapi.get_everything(q='entertainment',
#                               sources='bbc-news,abc-news,cnn,usa-today',
#                               domains='bbc.co.uk,techcrunch.com',
#                               #   from_param='2020-12-01',
#                               #   to='2020-12-12',
#                               language='en',
#                               sort_by='relevancy',
#                               page=2)

# news = newsapi.get_everything(q='entertainment',
#                               sources='bbc-news,the-verge',
#                               domains='bbc.co.uk,techcrunch.com',
#                               language='en',
#                               sort_by='relevancy',
#                               page=2)
