from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts import views as account_views

app_name = 'accounts'

urlpatterns = [
    path('register/', account_views.register, name='register'),
    path('accounts/profile/', account_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('', account_views.home, name='home')
]
