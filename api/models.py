from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=[('macho', 'Macho'), ('hembra', 'Hembra')])
    descripcion = models.TextField(blank=True)    
    imagen = models.ImageField(upload_to='mascotas/', null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.nombre