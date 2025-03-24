from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from aplicacioncita.models import Frutas

# Create your views here.
def fruta_form(request: HttpRequest) -> HttpResponse:
    return render(request, 'fruteria.html')

def fruta(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        nombre: str = request.POST['nombre']
        precio: float = float(request.POST['precio'])
        distribuidora: str = request.POST['distribuidora']

        fruta: Frutas = Frutas.objects.create(
               nombre=nombre, 
               precio=precio, 
               distribuidora=distribuidora
            )
        
        fruta.save()
        
    frutas: dict[str, str] = Frutas.objects.all()
    return render(request, 'frutas.html', {'frutas': frutas})

def eliminar_fruta(request: HttpRequest, fruta_id: int) -> HttpResponse:
    fruta = Frutas.objects.get(id=fruta_id)
    fruta.delete()
    return redirect('frutas')

def modificar_fruta(request: HttpRequest, fruta_id: int) -> HttpResponse:
    fruta = Frutas.objects.get(id=fruta_id)
    if request.method == 'POST':
        fruta.nombre = request.POST['nombre']
        fruta.precio = float(request.POST['precio'])
        fruta.distribuidora = request.POST['distribuidora']
        fruta.save()
        return redirect('frutas')
    return render(request, 'fruteria.html', {'fruta': fruta})

def form(request: HttpRequest) -> HttpResponse:
    username: str | None = None
    if request.method == "POST":
        username= request.POST['username']
        pswd: str = request.POST['password']
        user: User | None = authenticate(request, username=username, password=pswd)
        if username is not None:
            login(request, user)
            return HttpResponse("Usuario autenticado")
    return render(request, 'index.html')

def add_usuario(request):
    User.objects.create_user('Avrilsota', 'Avrilsita@gmail.com', 'Avrilsita123')
    return HttpResponse('Datos guardados satisfactoriamente')

def update_email(response: HttpResponse):
    u: User = User.objects.get(username='Avrilsota')
    u.email = 'Avrilsita@outlook.com'
    u.save()
    return HttpResponse('Usuario actualizado correctamente')

def authentication(request: HttpRequest):
    username: str | None = request.POST.get('username')
    password: str | None = request.POST.get('password')
    if username and password:
        u: User | None = authenticate(request, username=username, password=password)
    else:   
        u = authenticate(request, username='Avrilsita', password='Avrilsita123')
    if u:
        login(request, u)
        return HttpResponse('Usuario autenticado')
    return HttpResponse('Usuario no autenticado')

def logout_view(request):
    logout(request)
    return HttpResponse("Usuario deslogueado!")
