from io import StringIO
from PIL import Image

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile

class ConsejoRegional(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    CPsP = models.IntegerField(unique=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha_incorporacion = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    consejo_regional = models.ForeignKey(ConsejoRegional)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    direccion = models.CharField(max_length=512, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        self.direccion = self.direccion.upper()

        super(Persona, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombres + " " + self.apellidos
