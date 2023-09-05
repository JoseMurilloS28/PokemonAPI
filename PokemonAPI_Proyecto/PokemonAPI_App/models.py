from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Importacion  de las clases y funciones que sirviran con la autenticación de los usuarios,
# en Django se utilizan para crear modelos de usuario personalizados.


#  ***********************************************************
#  *  Corresponde a la creación de una clase que utiliza la  *
#  *  función "BaseUserManager", esta clases sirve para la   *
#  *  creación y gestión de usuarios en la aplicación.       *
#  ***********************************************************
class CrearUsuario(BaseUserManager):
    
    # Se define el metodo para crear los usuarios.
    def crear_usuario(self, nombre_usuario, correo_usuario, password_usuario = None, **extra_fields):
        
        #Se comprueba si el correo es ingresado.
        if not correo_usuario:
            raise ValueError('El correo electronico es obligatorio')
        
        #Se comprueba si el nombre de usuario es ingresado.
        if not nombre_usuario:
            raise ValueError('El nombre de usuario es obligatorio')
        
        #El correo electronico ingresado se convierte en minusculas.
        email_usuario =  self.normalize_email(correo_usuario)
        
        #Se crea una instancia del modelo con los datos ingresados.
        usuario = self.model(correo_usuario = email_usuario, nombre_usuario = nombre_usuario, **extra_fields)
        
        #Establece la contraseña ingresada (de forma segura con hash y salting).
        usuario.set_password(password_usuario)
        
        #Guarda la instancia del usuario en la base de datos.
        usuario.save(using=self._db)
        
        #devuelve la instancia creada.
        return usuario
    
    
    
#  ***********************************************************
#  *  Corresponde a la creación de una clase que sirve para  *
#  *  definir el modelo de Usuarios, que define los campos   *
#  *  esenciales para el usuario.                            *
#  ***********************************************************
class Usuarios(AbstractBaseUser, PermissionsMixin):
    
    #Define el campo 'correo_usuario' para almacenar un correo electronico de manera unica.
    correo_usuario = models.EmailField(unique=True)
    
    #Define el campo 'nombre_usuario' para almacenar nombres de usuarios unicos.
    nombre_usuario = models.CharField(max_length=30, unique=True)
    
    #Define el campo 'esta_activa' que indica si la cuenta esta activa (por defecto es True).
    esta_activa = models.BooleanField(default=True)
    
    #Creacion de un objeto para la creacion y gestionar usuarios.
    objects = CrearUsuario()
    
    #Define que 'USERNAME_FIELD' especificara que el inicio de sesion se basa en el campo de 'correo_usuario'.
    USERNAME_FIELD = 'correo_usuario'
    
    #Define que 'REQUIRED_FIELD' es una lista de campos adiccionales para la creacion de usuarios.
    REQUIRED_FIELDS = ['nombre_usuario']
    
    # Devuelve la representación de cadena de la instancia de CrearUsuario.
    def __str__(self):
    # En este caso se utiliza el campo 'correo_usuario' como representación.
        return self.correo_usuario