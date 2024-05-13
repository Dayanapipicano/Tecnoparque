from django.urls import path
from apps.gestiones.views import Home


app_name = 'gestiones'

urlpatterns = [
        path('', Home, name='home'), 
        #path('login/', login, name='login' ),
        #path('logaut/', logaut, name='logaut'),
        #path('cambiar_contraseña/', cambiar_contraseña, name='cambiar_contraseña'),
]
