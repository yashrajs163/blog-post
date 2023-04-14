from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm , PasswordChangeForm
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from .forms import SignUpForm , UpdateUserForm
from django.contrib import messages
from blobing.models import Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
# Create your views here.

def signup_view(request):
    if request.method== "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Welcome to the Blobing Blog.')
            return redirect ('blobing:home')    
    else:
        form = SignUpForm()
        # messages.warning(request, 'Fill the details correctly')    
    return render (request, 'accounts/signup.html',{'form':form})
    

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                messages.success(request, 'Welcome to the Blobing Blog')
                return redirect ('blobing:home')
    else:
        form = AuthenticationForm()
    return render (request, 'accounts/login.html',{'form':form,})    

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, ' You have been Logged Out ')
        return redirect ('blobing:home')

def profile(request, user_name):
    user_related_data = Article.objects.filter(author__username=user_name)

    return render(request, 'accounts/profile.html', {'user_related_data':user_related_data })

def edit_profile(request ,  username):
    form = UpdateUserForm()
    if request.method == 'POST':
        form = UpdateUserForm(request.POST , username=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return ('update_profile_success')
    else:
        form = UpdateUserForm()
    return render(request, 'accounts/edit_profile.html', {'form':form})


def change_password(request , user ):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been changed")
            return redirect('accounts:login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = PasswordChangeForm(user)
    return render(request, 'accounts/change_password.html', {'form': form})
    # if request.method== 'POST':
    #     form = PasswordChangeForm(request.POST , request.user)
    #     if form.is_valid():
    #         user = form.save()
    #         update_session_auth_hash(request, user)
    #         messages.success(request, 'Your password was successfully updated!')
    #         return redirect('accounts:profile')
    #     else:
    #         messages.success(request, 'error')
    # else:
    #     form = PasswordChangeForm(request.user)            
    # return render(request , 'accounts/change_password.html', {'form':form} )



def delete_profile(request , username):
    if request.method == 'POST':
        user = User.objects.get(username=username)
        user.delete()
        messages.success(request, ' You account has been delete.')
        return redirect('accounts:login')
    return render(request, 'accounts/deleteaccount.html',)