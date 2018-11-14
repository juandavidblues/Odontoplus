from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse('hola mundo')

def login(request):
    return HttpResponse('aqui te logueas mamaguevo')

# Create your views here.
