from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Receita
from receitas.models import Receita
from django.contrib.auth.models import User

def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    dados = {
        'receitas':receitas
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita':receita
    }
    
    return render(request, 'receita.html', receita_a_exibir)


def buscar(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas': lista_receitas
    }

    return render(request, 'buscar.html', dados)


def salvar_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        receita_id = request.POST['receita_id']
        user = get_object_or_404(User, pk=request.user.id)

        if receita_id:
            r = Receita.objects.get(pk=receita_id)
            r.nome_receita = nome_receita
            r.ingredientes = ingredientes
            r.modo_preparo = modo_preparo
            r.tempo_preparo = tempo_preparo
            r.rendimento = rendimento
            r.categoria = categoria
            r.foto_receita = foto_receita
                            
            r.save()
            return redirect('dashboard')

        else:
            receita = Receita.objects.create(
                pessoa=user,
                nome_receita=nome_receita,
                ingredientes=ingredientes,
                modo_preparo=modo_preparo,
                tempo_preparo=tempo_preparo,
                rendimento=rendimento,
                categoria=categoria,
                foto_receita=foto_receita
                )
            receita.save()
            return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')







