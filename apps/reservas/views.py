from django.shortcuts import render, redirect
from apps.reservas.models import Rol,TipoDocumento,Cargo
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

def create_tipo_documento(request):
    
    nombre = TipoDocumento.POST.get('nombre')
    if request.method == 'POST':
        tipo_documento = TipoDocumento.objects.create(
            nombre = nombre
        )
        
        return redirect('listar_tipo_documento')
    
    return render(request,'TipoDocumento/create_tipo_documento.html')

#FUNCION DE ACTUALIZAR TIPO DOCUMENTO
        
def update_tipo_documento(request,id):
    
    tipo_documento = TipoDocumento.objects.get('nombre')
    
    if request.method == 'POST':
        nombre = nombre
        
        tipo_documento.nombre = nombre
        tipo_documento.save()
    
        return redirect('listar_tipo_documento')
    return render(request, 'TipoDocumento/update_tipo_documento.html', {'tipo_documento':tipo_documento})

#FUNCION DE ELIMINAR TIPO DE DOCUMENTO
def delete_tipo_documento(request,id):
    tipo_documento = TipoDocumento.objects.get(id=id)
    if request.method == 'GET':
        tipo_documento.delete()
        
        return redirect('listar_tipo_documento')

#FUNCION DE LISTAR TIPO DE DOCUMENTO
def listar_tipo_documento(request):
    tipo_documento = TipoDocumento.objects.all()
    
    paginate = Paginator(tipo_documento,10)
    
    page_number = request.GET.get('page')
    page_obj =  paginate.get_page(page_number)
    
    return render(request, 'TipoDocumento/listar_tipo_documento', {'page_obj':page_obj}, {'tipo_documento':tipo_documento})

#FUNCIONES DE CARGO 

#FUNCION DE CREAR CARGO

def create_cargo(request):
    
    nombre = Cargo.POST.get('nombre')
    
    if request.method == 'POST':
        
        cargo = request.objects.create(
            nombre = nombre
        )
        return redirect('listar_cargo')
    
    return render(request, 'Cargo/create_cargo.html')

def update_cargo(request,id):
    cargo = Cargo.objects.get(id=id)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        
        cargo.nombre = nombre
        
        return redirect('listar_cargo')
    return render(request,'Cargo/update_cargo.html', {'cargo':cargo})

def delete_cargo(request,id):
    
    cargo = Cargo.objects.get(id=id) 
    
    if request.method == 'GET':
        cargo.delete
        
        return redirect('listar_cargo')

def listar_cargo(request,id):
    
    cargo = Cargo.objects.all()
    
    paginacion = Paginator(cargo,10)
    
    page_number = request.GET.get('page')
    page_obj = paginacion.get_page(page_number)
    
    return render(request,'Cargo/listar_cargo', {'page_obj':page_obj}, {'cargo':cargo})
