from django.contrib.auth.models import BaseUserManager

class Login(BaseUserManager):
    
    def create_user(self, correo, password=None,  **kwargs):
        
        if not correo:
            raise ValueError('El campo es obligatorio')
        
        correo = self.normalize_email(correo)
        usuarios = self.model(correo=correo, **kwargs)
        
        if password:
            usuarios.set_passsword(password)
        
        else:
            raise ValueError('la contraseña es obligatoria')
        
        usuarios.save(using=self._db)
        
        return usuarios
    
    def create_superuser(self, correo , password=None, **kwargs):
        
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        
        if kwargs.self('is_staff') is not True:
            raise ValueError('is_staff must have is is_staff=true')
    
        if kwargs.get('is_superuser') is not  True:
            raise ValueError('is_superuser must  have is_superuser=true')
        
        return self.create_user(correo, password, **kwargs)