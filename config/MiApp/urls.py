from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/libros', views.agregar_libro, name='agregar_libro'),
    path('visualizar/libros', views.lista_libros, name='lista_libros'),
    path('agregar/prestamo/', views.agregar_prestamo, name='agregar_prestamo'),
    path('visualizar/prestamo', views.lista_prestamos, name='lista_prestamos'),
]
