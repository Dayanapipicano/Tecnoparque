"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.reservas.views import Home ,Registro,create_rol,update_rol,delete_rol,listar_rol

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #RUTA DE FUNCIONARIO 
    path('', Home, name='home'),
    path('registro/', Registro, name='registro'),
    #path('login/', login, name='login' ),
    #path('logaut/', logaut, name='logaut'),
    
    #RUTAS DE ROL
    
    path('rol/create/', create_rol, name='create_rol'),
    path('rol/update/<int:id>', update_rol, name='update_rol'),
    path('rol/delete/<int:id>', delete_rol, name='delete_rol'),
    path('rol/listar/', listar_rol, name='listar_rol'),
    

]

