from django.shortcuts import render

import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .forms import CustomUserCreationForm, LaptopForm, UserPerfilform


def Home(request):
    return render(request,'home.html')

def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login.html')



@login_required
def profile(request):
    """
    perfil
    """
    form=UserPerfilform()
    if request.method == "POST":
        #Sim esta la imagen la reemplaza de lo contrario la crea
        try: #avatar anterior

            Userperfil=UserPerfil.objects.get(user=request.user)
            form=UserPerfilform(request.POST,request.FILES,instance=Userperfil)
            #Eliminar el avatar anterior, obtenemos el path
            pathAvatarViejo=os.path.join(settings.MEDIA_ROOT,Userperfil.avatar.name)

        except ObjectDoesNotExist:
            form=UserPerfilform(request.POST,request.FILES)

        if form.is_valid():
            #Preguntamos si existe el avatar viejo
            if pathAvatarViejo is not None and os.path.isfile(pathAvatarViejo):
                os.remove(pathAvatarViejo)
            userProfile=form.save(commit=False)
            userProfile.user=request.user
            userProfile.save()

    return render(request, 'registration/profile.html',{'form':form})