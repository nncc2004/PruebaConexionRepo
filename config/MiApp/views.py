from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.


def home(request):
    contexto = {
        'texto': "Hola Mundo!!!"
    }
    return render(request, "home.html", contexto)

def agregar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_libro') 
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, "lista_libros.html", {"libros": libros})


def agregar_prestamo(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_prestamo')
    else:
        form = PrestamoForm()
    return render(request, "agregar_prestamo.html", {"form": form})

def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, "lista_prestamos.html", {"prestamos": prestamos})