from django.db import models

# Create your models here.

class Libro(models.Model):
    codigo_libro = models.CharField(max_length=20, primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)

    #Gente, si alguien ve esto. Felicidades. Luego, puedes ignorar la siguiente parte, pues 
    #es sólo para el cómo se va a ver el nombre de la tabla en el django admin.
    def __str__(self):
        return f"{self.titulo} ({self.codigo_libro})"


class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True)
    rut_socio = models.CharField(max_length=12) 
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)  
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()

    #Gente, si alguien ve esto. Felicidades. Luego, puedes ignorar la siguiente parte, pues 
    #es sólo para el cómo se va a ver el nombre de la tabla en el django admin.
    def __str__(self):
        return f"Préstamo {self.id_prestamo} - {self.libro.titulo}"
