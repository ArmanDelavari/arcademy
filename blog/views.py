from django.shortcuts import render
from .models import *


# Create your views here.

def indexpage(request):
    all_articles = Article.objects.all().order_by('-created_at')[:9]
    context = {'all_articles': all_articles}
    return render(request, 'blog/index.html', context)