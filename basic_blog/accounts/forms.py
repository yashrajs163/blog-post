from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User  
# from django.contrib.auth.forms import UserCreationForm
      
class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class':'form-control','Placeholder': 'Enter username'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control','Placeholder': 'Enter your first name here'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','Placeholder': 'Enter your last name here'})
        self.fields['email'].widget.attrs.update({'class':'form-control','Placeholder': 'Enter your E-Mail here'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','Placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','Placeholder': 'Confirm your Password'})


    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
       
class UpdateUserForm(UserChangeForm):
   
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']