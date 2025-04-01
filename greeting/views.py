from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
import random

def hello_user(request):
    name = request.GET.get('name','web-traveler')
    message = request.GET.get('message', 'Это моя работа на пути к успеху :)')

    return render(request, 'greeting/beauty.html', {'name': name, 'message': message})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'greeting/register.html', {'form': form})

def secretcode(request):
    code = random.randint(1000, 9999)
    return render(request, 'greeting/secretcode.html', {'secretcode': code})


def custom_logout(request):
    # Сохраняем текущий URL в сессии для редиректа после выхода
    next_page = request.GET.get('next', request.META.get('HTTP_REFERER'))

    # Осуществляем выход пользователя
    logout(request)

    # Перенаправляем пользователя на предыдущую страницу или на главную, если next не указан
    return HttpResponseRedirect(next_page if next_page else '/')
