from django import forms
from .models import Item, Atividade

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome']

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['cidade']
