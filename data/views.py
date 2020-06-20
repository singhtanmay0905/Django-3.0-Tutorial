from django.shortcuts import render
from data.models import Article
# Create your views here.

def index(request):
    return render(request, 'data/index.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'data/list.html', {'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'data/detail.html', {'article': article})

