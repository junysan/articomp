from django.contrib import  admin
from .models import Publicacion,Tipo_Publicacion

admin.site.register(Tipo_Publicacion)
admin.site.register(Publicacion)