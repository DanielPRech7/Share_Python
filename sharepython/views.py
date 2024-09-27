from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm, AtividadeForm, Atividade
from django import forms

def lobby_view(request):
    return render(request, 'lobby.html')

def resumo_view(request):
    filtro = request.GET.get('filtro', None)

    if filtro == 'nova_tarefa':
        itens = Item.objects.all()
        atividades = None  # Não mostrar atividades

    elif filtro == 'nova_atividade':
        atividades = Atividade.objects.all()
        itens = None  # Não mostrar itens

    else:
        itens = Item.objects.all()
        atividades = Atividade.objects.all()

    return render(request, 'resumo.html', {'itens': itens, 'atividades': atividades, 'filtro': filtro})
def nova_tarefa_view(request):
    itens = Item.objects.all()
    return render(request, 'nova_tarefa.html', {'itens': itens})

def cadastrar_item_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nova_tarefa')
    else:
        form = ItemForm()

    return render(request, 'cadastrar_item.html', {'form': form})

def editar_tarefa_view(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('nova_tarefa')
    else:
        form = ItemForm(instance=item)
    return render(request, 'editar_tarefa.html', {'form': form, 'item': item})

def excluir_tarefa_view(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('nova_tarefa')
    return render(request, 'excluir_tarefa.html', {'item': item})

def atividades_view(request):
    atividades = Atividade.objects.all()
    return render(request, 'nova_atividade.html', {'atividades': atividades})

def cadastrar_atividade_view(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades')  # Redireciona para a lista de atividades
    else:
        form = AtividadeForm()

    return render(request, 'cadastrar_atividade.html', {'form': form})

def editar_atividade_view(request, atividade_id):
    atividade = Atividade.objects.get(id=atividade_id)
    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect('atividades')
    else:
        form = AtividadeForm(instance=atividade)
    return render(request, 'editar_atividade.html', {'form': form, 'atividade': atividade})

def excluir_atividade_view(request, atividade_id):
    atividade = Atividade.objects.get(id=atividade_id)
    if request.method == 'POST':
        atividade.delete()
        return redirect('atividades')
    return render(request, 'excluir_atividade.html', {'atividade': atividade})