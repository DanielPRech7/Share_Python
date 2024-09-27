from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Atividade(models.Model):
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.cidade
