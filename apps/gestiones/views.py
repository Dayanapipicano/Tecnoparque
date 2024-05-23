from django.shortcuts import render

def Home(request):
    return render(request,'home.html')

def registro(request):
    return render(request, 'registro.htrml')