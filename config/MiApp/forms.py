from django import forms
from .models import Libro, Prestamo

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['codigo_libro', 'titulo', 'autor']


class PrestamoForm(forms.ModelForm):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_termino = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Prestamo
        fields = ['rut_socio', 'libro', 'fecha_inicio', 'fecha_termino']