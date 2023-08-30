from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import RegisterForm, AuthForm

# Контроллер регистрации пользователя
def register_view(request):
    if request.method == 'GET':
        context_data = {
            'form': RegisterForm()
        }
        return render(request, 'users/register.html', context=context_data)

    if request.method == 'POST':
        data = request.POST
        form = RegisterForm(data=data)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            if cleaned_data['password1'] == cleaned_data['password2']:
                User.objects.create_user(username=cleaned_data['username'], password=cleaned_data['password1'])
                return redirect('/users/auth/')
            else:
                form.add_error('password2', 'Пароли не совпадают')

        context_data = {
            'form': form,
        }
        return render(request, 'users/register.html', context=context_data)

# Контроллер авторизации пользователя
def auth_view(request):
    if request.method == 'GET':
        context_data = {
            'form': AuthForm()
        }
        return render(request, 'users/auth.html', context=context_data)

    if request.method == 'POST':
        data = request.POST
        form = AuthForm(data=data)
        
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user:
                login(request=request, user=user)
                return redirect('/products/')
            else:
                form.add_error('username', 'Неверное имя пользователя или пароль')

        context_data = {
            'form': form,
        }
        return render(request, 'users/auth.html', context=context_data)

def logout_view(request):
    logout(request)
    return redirect('/products/')
