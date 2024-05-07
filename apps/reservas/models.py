from django.db import models
from django.contrib.auth.models import AbstractBaseUser
class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=100)
    
class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    
class Dependencia(models.Model):
    nombre = models.CharField(max_length=100)
    
class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    
    


