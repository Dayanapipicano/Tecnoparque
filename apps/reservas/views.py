from django.shortcuts import render, redirect
from apps.reservas.models import Rol
from django.core.paginator import Paginator
def Home(request):
    return render(request,'home.html')
    
def Registro(request):
    return render(request,'registro.html')


#FUNCIONES DE ROL

#FUNCION CREAR ROL
def create_rol(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        rol = Rol.objects.create(
            nombre = nombre
        )
        
        return redirect('listar_rol')
    else:
        return render(request,'Rol/rol_create.html')
    
#FUNCION EDITAR ROL

def update_rol(request, id):
    
    rol =  Rol.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        
        rol.nombre = nombre
        rol.save()
        return redirect('listar_rol')
    
    
    return render(request, 'Rol/update_rol.html', {'rol':rol})
    
#FUNCION ELIMINAR ROL 

def delete_rol(request,id):
    rol = Rol.objects.get(id=id)
    
    if request.method == 'GET':
        rol.delete()
    
    return redirect('Rol/listar_rol')


#FUNCION LISTAR ROL
def listar_rol(request):
    rol = Rol.objects.all()
    
    paginacion = Paginator(rol,10)
    
    page_numeber = request.GET.get('page')
    page_obj = paginacion.get_page(page_numeber)
    
    return render(request,'Rol/listar_rol.html',{'page_obj':page_obj}, {'rol':rol})


#FUNCIONES DE TIPO DE DOCUMENTO 

#FUNCION DE CREAR TIPO DE DOCUMENTO