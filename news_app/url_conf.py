from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
import requests
import time

def make_url(user, country='in'):
    category_list = {'3': 'business', '4': 'sports', '5': 'health', '6': 'entertainment'}

    if user == '2':
        country = 'us'

    if user == '1' or user == '2':
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey=bee8cc25aa844bc8bceff7d06367d0a8'
        articles = get_articles(url)
        return articles, user
    else:
        category = category_list[user]
        url = f'https://newsapi.org/v2/top-headlines/sources?category={category}&apiKey=bee8cc25aa844bc8bceff7d06367d0a8'
        articles = get_articles(url)
        return articles, user

def get_articles(url):
    response = requests.get(url)
    articles_list = []  # Initialize an empty list to store articles or sources

    try:
        data = response.json()

        if 'articles' in data:
            articles = data['articles']
            for i, article in enumerate(articles):
                title = article.get('title', '')
                author = article.get('author', 'unknown')
                description = article.get('description', '')
                url = article.get('url', '')
                articles_list.append({
                    'title': title,
                    'author': author,
                    'description': description,
                    'url': url,
                })
                # print(f"{title}\nAuthor: {author}\n{description}\nLink: {url}\n\n")
                # time.sleep(0.10)
        elif 'sources' in data:
            sources = data['sources']
            for i, source in enumerate(sources):
                name = source.get('name', '')
                description = source.get('description', '')
                url = source.get('url', '')
                articles_list.append({
                    'name': name,
                    'description': description,
                    'url': url,
                })
                # print(f"{name}\n{description}\nLink: {url}\n\n")
                # time.sleep(0.10)
        else:
            raise ValueError('No articles or sources found in the response')

        

    except Exception as e:
        print(f"Error processing response: {e}")

    return articles_list
