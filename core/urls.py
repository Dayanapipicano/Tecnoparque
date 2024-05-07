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
from apps.reservas.views import Home ,Registro
from apps.reservas import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    #RUTA DE FUNCIONARIO 
    path('', Home, name='home'),
    path('registro/', Registro, name='registro'),
    #path('login/', login, name='login' ),
    #path('logaut/', logaut, name='logaut'),
    
    
    
    #RUTAS DE ROL
    
    path('rol/create/', views.create_rol, name='create_rol'),
    path('rol/listar/', views.listar_rol, name='listar_rol'),
    path('rol/update/<int:id>', views.update_rol, name='update_rol'),
    path('rol/delete/<int:id>', views.delete_rol, name='delete_rol'),
    
    #RUTAS DE TIPO DOCUMENTO
    
    path('TipoDocumento/create/', views.create_tipo_documento, name='create_tipo_documento'),
    path('TipoDocumento/update/<int:id>', views.update_tipo_documento, name='update_tipo_documento'),
    path('TipoDocumento/delete/<int:id>', views.delete_tipo_documento, name='delete_tipo_documento'),
    path('TipoDocumento/listar/', views.listar_tipo_documento, name='listar_tipo_documento'),
    
    #RUTAS DE CARGO
    
    path('cargo/create', views.create_cargo, name='create_cargo'),
    path('cargo/update', views.update_cargo, name='update_cargo'),
    path('cargo/delete', views.delete_cargo, name='delete_cargo'),
    path('cargo/listar', views.listar_cargo, name='listar_cargo'),
    

]

