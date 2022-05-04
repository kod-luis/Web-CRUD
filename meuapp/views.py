from django.shortcuts import render, redirect, get_object_or_404
from .models import Animais
from .forms import AnimaisForm
from django.views.generic import ListView, DetailView

# Create your views here.
class IndexView(ListView):
    template_name = 'crud/index.html'
    context_object_name = 'animais_list'
    
    def get_queryset(self):
        return Animais.objects.all()

def infoview(request, pk, template_name='crud/info.html'):
    post = get_object_or_404(Animais, pk=pk)
    form = AnimaisForm(request.POST or None, instance=post)
    return render(request, template_name, {'form':form})

'''def IndexView(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos'})'''