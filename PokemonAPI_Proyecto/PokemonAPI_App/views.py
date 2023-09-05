# Corresponde a la importancion de funciones utiles de Django para las plantillas HTML.
from django.shortcuts import render, redirect

#Corresponde a la importancion de decorador para auntentificacion de usuarios en cada vista.
from django.contrib.auth.decorators import login_required

# Corresponde de igual manera para la auntentificacion del ususario para iniciar sesion.
from django.contrib.auth import login, authenticate

# Se utiliza para permitir que un usuario cierre sesión en la aplicacion.
from django.contrib.auth import logout

# Corresponde a la importancion de la biblioteca 'requests' útil para solicitudes de la API.
import requests


# Corresponde a la importancion de los formularios.
from .forms import RegistroUsuarioForm, InicioSesionForm


# Correspoden a la URL base de la API.
POKEAPI_URL = 'https://pokeapi.co/api/v2/pokemon/'



#  ***********************************************************
#  *  Corresponde a la vista principal, la cual mostrara     *
#  *  los pokemones para poder visualizarlos.                *
#  ***********************************************************
def pagina_principal(request):

    # Obtener los datos de la API para obtener los 20 Pokémon (GET).
    respuesta = requests.get(POKEAPI_URL)

    # Obtener los datos JSON y se guarda en la variable 'informacion'.
    informacion = respuesta.json()

    # Se extraen los resultados de la respuesta JSON y se crea una lista vacia por defecto.
    resultados = informacion.get('results', [])

    # Se crea un contexto el cual obtiene los resultados de la API para la plantilla HTML.
    contexto = {
        'resultados': resultados,
    }

    # Corresponde a renderizar la plantilla HTML y pasa el contexto como un diccionario.
    return render(request, 'index.html', contexto)



#  ***********************************************************
#  *  Corresponde a la vista para visualizar el pokemon que  *
#  *  el usuario eligio para ver sus caracteristicas.        *
#  ***********************************************************
@login_required  #Decroador de auntentificacion para la vista visualizar pokemon.

def visualizar_pokemon(request, pokemon_name):
    
    # Hacer una solicitud a la API de Pokémon para obtener los detalles del Pokémon
    respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/")
    
    # verifica si la respuesta de la API fue recibida correctamente y no hubo errores en la solicitud.
    if respuesta.status_code == 200:
        
        # Para obtener datos JSON y guardar en 'info_pokemon'.
        info_pokemon = respuesta.json()
        
        # Prepara los datos para ser enviados a la plantillla HTML.
        contexto = {
            
            #Los detalles del pokemon se almacenan en el contexto.
            'pokemon': info_pokemon, 
        }
        
        # Renderiza la platilla HTML con los datos.
        return render(request, 'visualizar_pokemon.html', contexto)
    else:
        
        # Mostrar un mensaje de error en la misma página si la solicitud no fue exitosa.
        error_mensaje = f"No se pudo encontrar información para el Pokémon {pokemon_name}."
        contexto = {
            'error_message': error_mensaje,
        }
        return render(request, 'visualizar_pokemon.html', contexto)




#  ***********************************************************
#  *  Corresponde a la vista para el registro del usuario    *
#  *  en la aplicación.                                      *
#  ***********************************************************
def registro_usuario(request):

    # Verifica si la solicitud fue de tipo POST.
    if request.method == 'POST':
        
        # Crea una instancia del formulario para el registro de usuario con los datos ingresados.
        form = RegistroUsuarioForm(request.POST)
        
        # Verifica si el formulario es valido.
        if form.is_valid():
            
            # Si es valido almacena la informacion en la base de datos.
            user = form.save()
            
            # Después de un registro exitoso, redirige al usuario a la página de inicio de sesión.
            return redirect('inicio_sesion')
    
    #Si la solicitud no es de tipo POST recarga de nuevo el formulario.
    else:
        form = RegistroUsuarioForm()
    
    contexto = {'form': form}
    return render(request, 'registration/registrar.html', contexto)



#  ***********************************************************
#  *  Corresponde a la vista para el inicio de sesion del    *  
#  *  usuario en la aplicación.                              *
#  ***********************************************************
def inicio_sesion(request):
    
    # Verifica si la solicitud es de tipo POST.
    if request.method == 'POST':
        
        # Se crea una instancia del formulario para el inicio de sesion con los datos.
        form = InicioSesionForm(request, data=request.POST)
        
        # Verifica si el formulario es valido.
        if form.is_valid():
            
            # Si es valido el formulario va obtener el usuario y la contraseña de manera valida.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Verifica si la auntentificacion del usuario con los datos ingresados.
            user = authenticate(request, username=username, password=password)
            
            # Si fue verificado con exito iniciara sesion y enviara al usuario a la pagina principal.
            if user is not None:
                login(request, user)
                return redirect('pagina_principal')
    
    # Si la solicitud no es POST, crea una instancia vacía del formulario.
    else:
        form = InicioSesionForm()
    
    contexto = {
        'form': form,
    }
    
    #  Retornara la pagina para iniciar sesion nuevamente.
    return render(request, 'registration/login.html', contexto)



#  ***********************************************************
#  *  Corresponde a la vista para cerrar sesion del usuario  *  
#  *  en la aplicación.                                      *
#  ***********************************************************
def cerrar_sesion(request):
    
    # Cierra la ssesion del usuario utilizando la funcion logout.
    logout(request)
    
    # Cuando se cierre la sesion lo enviara a la pagina principal.
    return redirect('pagina_principal')