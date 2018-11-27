from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_django
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from odontoplus.core.models import User

class UserDetailView(DetailView):
    model = User
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UserListView(ListView):
    model = User
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['users'] = User.objects.all()
        return context

class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy('list')
    fields = ['username','email','password']
    print(super(CreateView,self).get_context_data())

class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('list')
    fields = ['username','email','password']
    template_name_suffix = '_update_form'

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('list')
    fields = ['username','email','password']
    template_name_suffix = '_confirm_delete'

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
def users(request):
    from odontoplus.core.models import User
    users =  User.objects.all()
    return render(request,'core/users.html',{
        'users':users
    })

@login_required
def panel_control(request):
    return HttpResponse('')