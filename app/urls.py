from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('signupvs',signupvs, name='signupvs'),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('welcome',welcome,name='welcome'),
    path('logoutvs', logoutvs, name='logoutvs')


]
