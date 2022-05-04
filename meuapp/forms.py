from django import forms
from .models import *

class AnimaisForm(forms.ModelForm):
    class Meta:
        model = Animais
        fields = ['nome', 'idade', 'tipo', 'raca', 'dono', 'telefone']
