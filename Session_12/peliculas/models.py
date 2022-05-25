from django.db import models

# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField()
    imagen = models.URLField()

    def __str__(self):
        return self.nombre + " " + self.apellidos 

class Pelicula(models.Model):
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=25)
    sinopsis = models.TextField(max_length=100, help_text='De que trata la pelicula')
    duracion = models.PositiveIntegerField(help_text='Cuanto dura la pelicula en minutos')
    imagen = models.URLField()
    anyo = models.PositiveIntegerField(help_text='Año de publicación de la pelicula')

    def __str__(self):
        return self.nombre