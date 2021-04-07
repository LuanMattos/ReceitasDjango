from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            return redirect('login')
        if User.objects.filter(email=email).exists():
             username = User.objects.filter(email=email).values_list('username', flat=True).get()
             user_logado = auth.authenticate(request, username=username, password=senha)
             if user_logado is not None:
                auth.login(request, user_logado)
        return redirect('dashboard')

    return render(request,'usuarios/login.html')


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        print('salvou')

        if not validate_form(request):
            return redirect('cadastro')
        else:
            return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

def logout(request):
    pass

def validate_form(req):

    if not req.POST['nome'].strip() or not len(req.POST['nome']):
        return False
    if not req.POST['email'].strip():
        return False
    if not req.POST['password'].strip():
        return False        
    if not req.POST['password2'].strip():
        return False        
    if req.POST['password'] != req.POST['password2']:
        return False

    return True