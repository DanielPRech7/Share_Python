from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm, AtividadeForm, Atividade
from django import forms

def lobby_view(request):
    return render(request, 'lobby.html')

def resumo_view(request):
    return render(request, 'resumo.html')

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
