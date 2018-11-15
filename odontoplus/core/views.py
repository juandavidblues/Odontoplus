from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse('hola mundo')

def login(request):
    if request.POST:
        print('hola')
    return render(request,'core/login.html',{})

# Create your views here.
