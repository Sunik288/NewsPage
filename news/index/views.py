from django.shortcuts import render
from .models import News, NewsCategory

def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {'news': news, 'categories': categories}
    return render(request, 'home.html', context)

def category_page(request, pk):
    news_category = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(news_category=news_category)

    context = {'news': news, 'category': news_category}

    return render(request, 'category.html', context)

def news_page(request, pk):
    news = News.objects.get(id=pk)
    category = NewsCategory.objects.get(category_name=news.news_category)

    context = {'news': news, 'category': category}

    return render(request, 'news.html', context)