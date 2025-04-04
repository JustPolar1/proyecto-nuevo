from django.shortcuts import render, redirect # Importar la función render y redirect de Django
from django.http import HttpResponse, HttpRequest # Importar las clases HttpResponse y HttpRequest de Django
# Importar las clases necesarias para la autenticación de usuarios y notacion de tipos
from django.contrib.auth.models import User, AbstractBaseUser
from django.db.models import QuerySet # Importamos QuerySet para la notación de tipos
from django.contrib.auth import authenticate, login, logout # Importar las funciones de autenticación de Django
from aplicacioncita.models import Frutas # Importar el modelo Frutas de la aplicación aplicacioncita

# ----------------------E-commerce-----------------------------

# Vista para renderizar el formulario de frutas
def fruta_form(request: HttpRequest) -> HttpResponse:
    return render(request, 'fruteria.html')

# Vista para guardar los datos de la fruta en la base de datos
# Se utiliza la función create() para crear un nuevo objeto de tipo Frutas
def fruta(request: HttpRequest) -> HttpResponse:
    # Si el método de la petición es POST, se obtienen los datos del formulario
    if request.method == 'POST':
        nombre: str = request.POST['nombre']
        precio: float = float(request.POST['precio'])
        distribuidora: str = request.POST['distribuidora']

        # Se utiliza la función create() para crear un nuevo objeto de tipo Frutas
        # Se utiliza la función objects.create() para crear un nuevo objeto de tipo Frutas
        fruta: Frutas = Frutas.objects.create(
               nombre=nombre, 
               precio=precio, 
               distribuidora=distribuidora
            )
        
        # Se utiliza la función save() para guardar el objeto en la base de datos
        fruta.save()
    
    # Lectura de datos
    frutas: QuerySet[Frutas, Frutas] = Frutas.objects.all()
    return render(request, 'frutas.html', {'frutas': frutas})

# Vista para eliminar una fruta de la base de datos
def eliminar_fruta(request: HttpRequest, fruta_id: int) -> HttpResponse:
    # Se utiliza la función get() para obtener el objeto de tipo Frutas
    # Se utiliza la función delete() para eliminar el objeto de la base de datos
    fruta = Frutas.objects.get(id=fruta_id) # Se obtiene el objeto de tipo Frutas utilizando la id
    fruta.delete()
    return redirect('frutas')

# Vista para modificar los datos de una fruta
def modificar_fruta(request: HttpRequest, fruta_id: int) -> HttpResponse:
    # Se utiliza la función get() para obtener el objeto de tipo Frutas
    # Se utiliza la función save() para guardar los cambios en la base de datos
    fruta = Frutas.objects.get(id=fruta_id)
    # Obtenemos los datos del formulario
    # Se utiliza el método POST para enviar los datos del formulario
    if request.method == 'POST':
        fruta.nombre = request.POST['nombre']
        fruta.precio = float(request.POST['precio'])
        fruta.distribuidora = request.POST['distribuidora']
        fruta.save()
        # Se redirige a la vista de frutas después de modificar los datos
        # Se utiliza la función redirect() para redirigir a la vista de frutas
        return redirect('frutas')
    return render(request, 'fruteria.html', {'fruta': fruta})

# ----------------------Usuarios-----------------------------

# Vista para renderizar el formulario de inicio de sesión
# Se utiliza la función render() de Django para renderizar el template index.html
def form(request: HttpRequest) -> HttpResponse:
    username: str | None = None
    # Se utiliza el método POST para enviar los datos del formulario
    if request.method == "POST":
        username = request.POST['username']
        pswd: str = request.POST['password']

        # Se utiliza la función authenticate() de Django para autenticar al usuario
        # Si el nombre de usuario y la contraseña son válidos, se autentica al usuario
        # Si no se envían, se utiliza un valor por defecto para autenticar al usuario
        # En este caso, se han puesto los valores de un usuario creado previamente
        user: AbstractBaseUser | None = authenticate(request, username=username, password=pswd)
        if username is not None:
            login(request, user)
            return HttpResponse("Usuario autenticado")
    return render(request, 'index.html')

def add_usuario(request: HttpRequest) -> HttpResponse:
    # Se utiliza la función create_user() para crear un nuevo usuario
    User.objects.create_user('Avrilsota', 'Avrilsita@gmail.com', 'Avrilsita123')
    return HttpResponse('Datos guardados satisfactoriamente')

# Vista para actualizar el email del usuario
# Se utiliza el método save() para guardar los cambios en la base de datos
def update_email(request: HttpRequest) -> HttpResponse:
    u: User = User.objects.get(username='Avrilsota')
    u.email = 'Avrilsita@outlook.com'
    u.save()
    return HttpResponse('Usuario actualizado correctamente')

# Vista para autenticar al usuario
# Se utiliza la función authenticate() de Django para autenticar al usuario
def authentication(request: HttpRequest) -> HttpResponse:
    # Se obtiene el nombre de usuario y la contraseña del formulario
    username: str | None = request.POST.get('username')
    password: str | None = request.POST.get('password')
    # Si el nombre de usuario y la contraseña son válidos, se autentica al usuario
    # Si no se envían, se utiliza un valor por defecto para autenticar al usuario
    if username and password:
        u: AbstractBaseUser | None = authenticate(request, username=username, password=password)
    else:   
        u = authenticate(request, username='Avrilsita', password='Avrilsita123')
    
    # Si el usuario es válido, se inicia sesión y se redirige a la página de inicio
    # Si no, se muestra un mensaje de error
    if u:
        login(request, u)
        return HttpResponse('Usuario autenticado')
    return HttpResponse('Usuario no autenticado')

# Vista para cerrar sesión
# Se utiliza la función logout() de Django para cerrar la sesión del usuario
def logout_view(request):
    logout(request)
    return HttpResponse("Usuario deslogueado!")

# ----------------------Mapa-----------------------------

# Vista para renderizar el mapa junto a las coordenadas dadas por el usuario
# Además tiene un valor por defecto para las coordenadas en caso de que no se envíen
# por el usuario. En este caso, se han puesto las coordenadas de la UTCH.
def coordinates(request: HttpRequest) -> HttpResponse:
    # Se utiliza QuerySet.get() para obtener los valores de latitud y longitud
    # con un segundo argumento que es el valor por defecto en caso de que no los encuentre
    latitud: str = request.GET.get('latitud', '28.6412257')
    longitud: str = request.GET.get('longitud', '-106.1488653')
    # Se renderiza el mapa.html con las coordenadas obtenidas
    return render(request, 'mapa.html', {'latitud': latitud, 'longitud': longitud})
