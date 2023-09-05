# Corresponde a la importanción del modulo de formularios de Django
from django import forms

# Corresponde a la importancion de formularios relacionado con la auntetificacion de Django.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Importancion del modelo personalizado para el usuario
from .models import Usuarios



#  ***********************************************************
#  *  Corresponde a la creacion del formulario para el       *
#  *  registro del usuario en la aplicación, el cual hereda  *
#  *  el UserCreationForm de Django.                         *
#  ***********************************************************
class RegistroUsuarioForm(UserCreationForm):
    
    #Campo para el correo electronico.
    correo_usuario = forms.EmailField(label="Ingrese su correo")
    
    #Campo para el nombre de usuario.
    nombre_usuario = forms.CharField(label="Ingrese su nombre de usuario")
    
    #Campos para ingresar las contraseñas que cuentas con unas widget para oculatar las contraseñas y texto de ayuda vacio.
    password1 = forms.CharField(label="Ingrese una contraseña", widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, help_text='')

    # Creacion de la clase 'Meta' para agregar mas informacion que debe contener el formulario.
    class Meta:
        
        # Usamos el modelo de 'Usuarios'.
        model = Usuarios
        
        # Creacion a los campos a llenar en el formulario.
        fields = ['correo_usuario', 'nombre_usuario', 'password1', 'password2']



#  ***********************************************************
#  *  Corresponde a la creacion del formulario para el       *
#  *  Inicio de sesion del usuario en la aplicación,         *
#  *  el cual hereda el AuthenticationForm de Django.        *
#  ***********************************************************
class InicioSesionForm(AuthenticationForm):
    
    # Creacion de la clase 'Meta' para agregar mas informacion que debe contener el formulario.
    class Meta:
        
        # Usamos el modelo personalizado de Usuarios
        model = Usuarios
        
        # Creacion a los campos a llenar en el formulario.
        fields = ['correo_usuario', 'password_usuario']