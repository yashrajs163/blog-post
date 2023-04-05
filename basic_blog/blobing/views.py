from django.shortcuts import render, redirect
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from . models import Article
from .  import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

def search_blogs(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        articles = Article.objects.filter(title__contains=searched)

        return render(request,'blobing/search.html', {'searched': searched,'articles':articles})
    else:
        return render(request,'blobing/search.html')


def home(request):
    article = Article.objects.all().order_by('-pub_date') #have removed this 
    # set up pagination
    p = Paginator(Article.objects.order_by('-pub_date'), 2) 
    page = request.GET.get('page')
    articles = p.get_page(page)
    nums = "a" * articles.paginator.num_pages

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request,'blobing/home.html', {'articles':articles,'nums':nums, 'num_visits':num_visits})
    
     

@login_required(login_url='/accounts/login')
def Articles(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            Instance=form.save(commit=False)
            Instance.author=request.user
            Instance.save()
            return redirect ('blobing:home')
    else:
        form = forms.CreateArticle()
    return render (request, 'blobing/index.html', {'form': form})


def details(request , id):
    article = Article.objects.get(id=id)
    return render (request, 'blobing/details.html', {'article': article})


