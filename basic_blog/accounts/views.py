from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.

def signup(request):
    if request.method== "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('blobing:home')    
    else:
        form = UserCreationForm()   
    return render (request, 'accounts/signup.html',{'form':form} )
