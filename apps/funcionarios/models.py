from django.db import models

class Base(models.Model):
    creacion = models.DateField(auto_now=True)
    actualizacion = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    

class TipoDocumento(Base):
    nombre = models.CharField(max_length=50)
    
class Cargo(Base):
    nombre = models.CharField(max_length=50)
    
class Dependencia(Base):
    nombre = models.CharField(max_length=50)
    
class Rol(Base):
    nombre = models.CharField(max_length=50)
    

class Persona(AbstractBaseUser):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    id_tipo_documento = models.OneToOneField(TipoDocumento,on_delete=models.CASCADE)
    identificacion = models.CharField(max_length=10)
    correo = models.EmailField(unique=True)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    id_dependencia = models.ForeignKey(Dependencia,on_delete=models.CASCADE)
    id_rol = models.OneToOneField(Rol,on_delete=models.CASCADE,)
