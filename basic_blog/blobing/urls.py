from django.urls import path
from . import views

app_name = 'blobing'

urlpatterns = [
    path('', views.home , name = 'home'),
    path('articles', views.Articles, name = 'articles'),
    path ('details/<int:id>' , views.details , name = 'details'),
    path ('search_blogs' , views.search_blogs , name = 'search-blogs'),     
]