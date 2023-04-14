from django.shortcuts import render, redirect
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from . models import Article
from .  import forms 
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib import messages

# Create your views here.

def search_blogs(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        articles = Article.objects.filter(title__contains=searched)
        messages.success(request, 'Your search request is ready.')
        return render(request,'blobing/search.html', {'searched': searched,'articles':articles})
    else:
        messages.warning(request, ' Search Correctly.')
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
            messages.info(request, 'Your Blog has been created successfully.')
            return redirect ('blobing:home')
        else:
            messages.warning(request, 'Something went wrong.')
    else:
        form = forms.CreateArticle()
    return render (request, 'blobing/index.html', {'form': form})


def details(request , id):
    # articles = Article.objects.all().order_by('pub_date')    
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404    
    return render (request, 'blobing/details.html', {'article': article})

def edit_blog(request, id):
    instance = Article.objects.get(id = id)
    if request.method == 'POST':
        form = forms.UpdateArticleForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.warning(request, str(form.errors))
            return render(request,'blobing/edit_blogs.html',{'form':form})
    else:
        form = forms.UpdateArticleForm(instance=instance)
    return render(request,'blobing/edit_blogs.html',{'form':form})

def delete_blog(request, id):
    if request.method == 'POST':
        object = Article.objects.get(id=id)
        object.delete()
        messages.success(request, 'Deleted succesfully')
        return redirect('home')
    else:
        messages.warning(request, 'error')
    return render(request, 'blobing/delete_blog.html')

      