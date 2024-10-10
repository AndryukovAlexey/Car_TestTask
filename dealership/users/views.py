from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegForm


def registr(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    else:
        error = None
        if request.method == 'POST':
            form = RegForm(request.POST)

            if form.is_valid():
                email = form.cleaned_data.get('email')

                if not User.objects.filter(email=email):

                    form.save()
                    return redirect('home-page')
                else:
                    error = 'Пользователь с такой почтой уже существует'
                
        else:
            form = RegForm()
        return render(request, 'users/registr.html', {'form': form, 'title': 'Регистрация','error': error})

class Auth(LoginView):
    template_name='users/auth.html'
    redirect_authenticated_user = True
    
    def get_context_data(self, **kwargs):
        ctx = super(Auth, self).get_context_data(**kwargs)
        ctx['title'] = 'Авторизация'
        return ctx
