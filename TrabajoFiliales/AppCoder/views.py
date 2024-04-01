from django.views.generic import ListView, CreateView
from .models import Usuario, Filial
from django.shortcuts import render



def inicio(request):
    return render(request, 'padre.html')

class RegistroView(CreateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'filial_asociada']
    template_name = 'registro.html'
    success_url = '/lista_usuarios/'

class RegistroFilialesView(CreateView):
    model = Filial
    fields = ['nombre_filial', 'direccion']
    template_name = 'registro_filiales.html'
    success_url = '/lista_filiales/'

class ListaUsuariosView(ListView):
    model = Usuario
    template_name = 'lista_usuarios.html'

class ListaFilialesView(ListView):
    model = Filial
    template_name = 'lista_filiales.html'