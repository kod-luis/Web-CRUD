from django.db import models

TIPOS = [
    ('', 'Escolha..'),
    ('1', 'Gato'),
    ('2', 'Cachorro'),
]

# Create your models here.
class Animais(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=TIPOS)
    raca = models.CharField(max_length=200)
    dono = models.CharField(max_length=200)
    telefone = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome
