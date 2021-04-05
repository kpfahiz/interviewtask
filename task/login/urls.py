from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .views import signUp,loginPage,home


app_name ='core'


urlpatterns = [
    path('',signUp,name="signup"),
    path('login/',loginPage,name="login"),
    path('home/',home,name="home")
]