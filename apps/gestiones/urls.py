from django.urls import path
from apps.gestiones import views

app_name = 'gestiones'

urlpatterns = [
        path('login/',views.login, name='login' ),
        path('registro/',views.registro, name='registro'),
        path('',views.Home, name='home'),
        #path('logaut/', logaut, name='logaut'),
        #path('cambiar_contraseña/', cambiar_contraseña, name='cambiar_contraseña'),
]
