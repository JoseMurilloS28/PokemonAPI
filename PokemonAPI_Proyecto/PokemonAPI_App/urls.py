from django.urls import path

# Sirve para la auntentificacion de ususarios en Django.
from django.contrib.auth import views as auth_views

# Importamos las views de nuestra App.
from . import views



#  ***********************************************************
#  *  Corresponde a la definicion de las rutas que se        *
#  *  usaran en el navegador para visualizar las views.      *
#  ***********************************************************
urlpatterns = [
    
    # Es una URL de Django que dirigirá a los usuarios a la vista de inicio 'accounts/login/'.
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    
    # Corresponde a la ruta de la pagina principal.
    path('', views.pagina_principal, name='pagina_principal'),
    
    # Ruta para visualizar un pokemon en especifico.
    path('pokemon/<str:pokemon_name>/', views.visualizar_pokemon, name='visualizar_pokemon'),
    
    # Ruta para registrar un usuario en la app.
    path('registro/', views.registro_usuario, name='registro_usuario'),
    
    # Ruta para la vista de inicio de sesion de la aplicacion.
    path('iniciar-sesion/', views.inicio_sesion, name='inicio_sesion'),
    
    # Ruta para la vista de cerrar sesion de la aplicacion.
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]