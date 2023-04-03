from django.shortcuts import render, redirect
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from . models import Article
from .  import forms

# Create your views here.

def search_blogs(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        articles = Article.objects.filter(title__contains=searched)

        return render(request,'blobing/search.html', {'searched': searched,'articles':articles})
    else:
        return render(request,'blobing/search.html')


def home(request):
    article = Article.objects.all().order_by('-pub_date')
    # set up pagination
    p = Paginator(Article.objects.order_by('-pub_date'), 5) 
    page = request.GET.get('page')
    articles = p.get_page(page)
    nums = "a" * articles.paginator.num_pages

    return render(request,'blobing/home.html', {'article':article,'articles':articles,'nums':nums})


def Articles(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('blobing:home')
    else:
        form = forms.CreateArticle()
    return render (request, 'blobing/index.html', {'form': form})


def details(request , id):
    article = Article.objects.get(id=id)
    return render (request, 'blobing/details.html', {'article': article})


