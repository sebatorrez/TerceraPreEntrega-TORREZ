from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('registro_filiales/', views.RegistroFilialesView.as_view(), name='registro_filiales'),
    path('lista_usuarios/', views.ListaUsuariosView.as_view(), name='lista_usuarios'),
    path('lista_filiales/', views.ListaFilialesView.as_view(), name='lista_filiales'),
]