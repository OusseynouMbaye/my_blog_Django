from django.urls import path
from .views import index, article

urlpatterns = [
    path('', index, name="blog-index"),
    # path('article-01/', article_01, name="blog-article-01"),
    path('article-<str:numero_article>/', article, name='blog-article')
]
