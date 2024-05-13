from django.urls import path
from apps.funcionarios import views

app_name = 'funcionarios'

urlpatterns = [
    
    path('registro/', views.Registro, name='registro'),
    
    
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
    path('cargo/update/<int:id>', views.update_cargo, name='update_cargo'),
    path('cargo/delete/<int_id>', views.delete_cargo, name='delete_cargo'),
    path('cargo/listar', views.listar_cargo, name='listar_cargo'),
    
    #RUTAS DE DEPENDENCIA
    
    path('dependencia/create', views.create_dependencia, name='create_dependencia'),
    path('dependencia/update/<int:id>', views.update_dependencia, name='update_dependencia'),
    path('dependencia/delete/int:id>', views.delete_dependencia, name='delete_dependencia'),
    path('dependencia/listar', views.listar_depemdencia, name='listar_dependencia'),
    
       
       
       
]
