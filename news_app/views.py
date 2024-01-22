from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
import requests
import time
import win32com.client
from .url_conf import *

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def index(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        articles, user = make_url(user)
        return render(request, 'articles.html', {'articles': articles, 'user': user})
    return render(request, 'index.html')

def articles(request, articles,user):
    print(articles,user)
    return render(request, 'articles.html', {'articles': articles, 'user': user})

