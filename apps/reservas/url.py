from django.urls import path
from apps.reservas import views

app_name = 'reservas'

urlpatterns = [
    
    
    # #RUTAS DE IMPLEMENTOS
    
    # path('implementos/create', views.create_implementos, name='create_implemento'),
    # path('implementos/update/<int:id>', views.update_implementos, name='update_implemento'),
    # path('implementos/delete/<int_id>', views.delete_implementos, name='delete_implemento'),
    # path('implementos/listar', views.listar_implementos, name='listar_implemento'),
    
    # #RUTAS DE ESPACIOS
    
    # path('espacios/create', views.create_espacios, name='create_espacio'),
    # path('espacios/update/<int:id>', views.update_espacios, name='update_espacio'),
    # path('espacios/delete/<int_id>', views.delete_espacios, name='delete_espacio'),
    # path('espacios/listar', views.listar_espacios, name='listar_espacio'),
    
    # #RUTAS DE RESERVAS
    
    # path('reservas/create', views.create_reservas, name='create_reserva'),
    # path('reservas/update/<int:id>', views.update_reservas, name='update_reserva'),
    # path('reservas/delete/<int_id>', views.delete_reservas, name='delete_reserva'),
    # path('reservas/listar', views.listar_reservas, name='listar_reserva'),
    
]
