from django.contrib import admin
from django.urls import path,include
from odontoplus.core.views import index,login,users_index

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('users', users_index, name='users')
]