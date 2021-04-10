from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

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
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        
    
        if not request.POST['nome'].strip() or not len(request.POST['nome']):
                messages.error(request, 'Nome é obrigatório')
                return redirect('cadastro')
        elif not request.POST['email'].strip():
                messages.error(request, 'Email é obrigatório')
                return redirect('cadastro')
        elif not request.POST['password'].strip():
                messages.error(request, 'Senhas é obrigatória')
                return redirect('cadastro')
        elif not request.POST['password2'].strip():
                messages.error(request, 'Senhas é obrigatória')
                return redirect('cadastro')        
        elif request.POST['password'] != request.POST['password2']:
                messages.error(request, 'Senhas não conferem')
                return redirect('cadastro')
        else:
            user = User.objects.create_user(username=nome, email=email, password=senha)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)
        dados = {
            'receitas':receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

def cria_receita(request):
    return render(request,'usuarios/cria_receita.html')

def deletar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def editar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {
        'receita': receita
    }
    return render(request,'usuarios/cria_receita.html', receita_a_editar)