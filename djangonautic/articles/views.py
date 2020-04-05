from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles_list.html', {'articles': articles})
