from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def lobby_view(request):
    return render(request, 'lobby.html')

def resumo_view(request):
    return render(request, 'resumo.html')

def nova_tarefa_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nova_tarefa')
    else:
        form = ItemForm()

    itens = Item.objects.all()

    return render(request, 'nova_tarefa.html', {'form': form, 'itens': itens})