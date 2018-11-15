from django.contrib import admin
from django.urls import path,include
from odontoplus.core.views import index,login

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login')
]