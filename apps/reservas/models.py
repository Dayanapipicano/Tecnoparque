from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from apps.funcionarios.models import Base,Persona

class Implementos(Base):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    referencia_serie = models.CharField(max_length=50)
    
    
class Espacio(Base):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    aforo_del_espacio = models.CharField(max_length=100)
    id_implementos = models.ForeignKey(Implementos,on_delete=models.CASCADE)
    
    
class Reservas(Base):
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    id_espacio = models.ForeignKey(Espacio,on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

