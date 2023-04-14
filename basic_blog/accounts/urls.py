from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/edit/<str:username>', views.edit_profile, name="edit_profile"),
    path('profile/<str:user_name>', views.profile, name="profile"),
    path('profile/password/<str:user>/', views.change_password, name="change_password"),
    path('delete/<str:username>/', views.delete_profile, name='delete'),

]