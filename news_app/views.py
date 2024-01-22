from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

from .url_conf import *



def index(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        articles, user = make_url(user)
        return render(request, 'articles.html', {'articles': articles, 'user': user})
    return render(request, 'index.html')

def articles(request, articles,user):
    print(articles,user)
    return render(request, 'articles.html', {'articles': articles, 'user': user})

