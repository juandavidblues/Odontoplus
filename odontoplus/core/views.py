from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_django
from django.shortcuts import redirect

@login_required
def index(request):
    return render(request,'core/index.html',{})

def login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.POST:
        if request.GET:
            next = request.GET.get('next')
        else:
            next = None
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login_django(request,user)
            if next:
                return HttpResponseRedirect(next)
            return redirect('index')
        else:
            return render(request,'core/login.html',{
                'next': request.GET.get('next')
            })

    return render(request,'core/login.html',{
        'next': request.GET.get('next')
    })

@login_required
def users_index(request):
    from odontoplus.core.models import User
    users =  User.objects.all()
    return render(request,'core/users.html',{
        'users':users
    })

@login_required
def panel_control(request):
    return HttpResponse('')

@login_required
def create_view(request):