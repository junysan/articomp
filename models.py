from django.db import models
from django.contrib.auth.models import User


class Tipo_Publicacion(models.Model):
    descripcion = models.CharField(max_length=60)
    estado = models.BooleanField
    def __str__(self):  # __unicode__ on Python 2
        return self.descripcion


class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    publicado_text = models.TextField
    tipo = models.ForeignKey(Tipo_Publicacion)
    fecha_publicacion = models.DateField('date publicado')
    usuario_pub = models.ForeignKey(User)
    def __str__(self):  # __unicode__ on Python 2
        return self.titulo