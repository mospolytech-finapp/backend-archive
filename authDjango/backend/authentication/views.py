from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import CustomUser
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        email = request.POST['email']
        date_of_birth = request.POST.get('date_of_birth', None)
        gender = request.POST['gender']
        password = request.POST['password']

        # Проверяем, заполнены ли все поля формы
        if not last_name or not first_name or not email or not password:
            messages.error(request, 'Пожалуйста, заполните все обязательные поля формы.')
            return render(request, 'register.html')

        # Проверяем, существует ли пользователь с такой почтой
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с такой почтой уже существует.')
            return render(request, 'register.html')

        CustomUser.objects.create_user(email=email, password=password,
                                       last_name=last_name, first_name=first_name,
                                       middle_name=middle_name, date_of_birth=date_of_birth,
                                       gender=gender)
        messages.success(request, 'Вы успешно зарегистрированы!')
        return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Неправильная пара логин-пароль'})
    else:
        return render(request, 'login.html')
