from django.shortcuts import render
from .models import *


# Create your views here.

def indexpage(request):
    all_articles = Article.objects.all().order_by('-created_at')[:9]
    all_promot_article = Article.objects.filter(promot=True)
    context = {'all_articles': all_articles, 'all_promot_article': all_promot_article}
    return render(request, 'blog/index.html', context)


def contactpage(request):
    return render(request, 'blog/page-contact.html')