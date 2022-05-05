from django.shortcuts import render, redirect, get_object_or_404
from .models import Animais
from .forms import AnimaisForm
from django.views.generic import ListView, DetailView

# Create your views here.
def listapet(request):
    animais = Animais.objects.all()
    return render(request, 'crud/index.html', {'animais':animais})

def saveform(request, pk=0, temp_name='crud/info.html'):
    if pk == 0: #adicionando
        if request.method == 'POST':
            form = AnimaisForm(request.POST)            
            if form.is_valid():
                form.save()
                return redirect('index')

        form = AnimaisForm()
    else: #editando
        animal = get_object_or_404(Animais, pk=pk)
        form = AnimaisForm(request.POST or None, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    return render(request, temp_name, {'form':form})

def deletapet(request, pk):
    animal = get_object_or_404(Animais, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('index')
    return render(request, 'crud/confirm_del.html', {'animal':animal})