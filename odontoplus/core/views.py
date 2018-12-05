from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_django
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import TemplateView

from odontoplus.core.forms import UserFrom
from odontoplus.core.models import User

@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    model = User
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context

@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model = User
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class UserCreateView(CreateView):
    model = User
    success_url = reverse_lazy('list')
    form_class = UserFrom
    verbose_name = 'Crear'
    model_name = 'Usuarios'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.verbose_name
        context['model'] = self.model_name
        return context

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('list')
    form_class = UserFrom
    template_name_suffix = '_update_form'
    verbose_name = 'Editar'
    model_name = 'Usuarios'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['view_name'] = self.verbose_name
        context['model'] = self.model_name
        return context

@method_decorator(login_required, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('list')
    fields = ['username','email','password']
    template_name_suffix = '_confirm_delete'


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'core/index.html'



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