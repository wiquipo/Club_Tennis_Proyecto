from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import Servicio, Contratacion
from .forms import ServicioForm, ContratacionForm

# Create your views here
def listaServicio(request):
    servicio=Servicio.objects.all()
    return render(request,"CrudServicio/listado.html",{'servicio':servicio})

def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')      
  
def crear_editarServicio(request,idServicio=0):
      if request.method=="GET":
        if idServicio==0:
            formulario=ServicioForm()   
        else:
            Servicioid=Servicio.objects.get(pk=idServicio)
            formulario=ServicioForm(instance=Servicioid)
        return render(request,'CrudServicio/Crear.html',{'formulario':formulario})
      else:
        if idServicio==0:
            formulario=ServicioForm(request.POST or None, request.FILES or None)
        else:
            Servicioid=Servicio.objects.get(pk=idServicio)
            formulario=ServicioForm(request.POST or None, request.FILES or None ,instance=Servicioid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaServicio')
        
def eliminarS(request, idServicio):
    bc=Servicio.objects.get(idServicio=idServicio)
    bc.delete()
    return redirect('listaServicio')
        
        

# Create your views here
def listaContratacion(request):
    contratacion=Contratacion.objects.all()
    return render(request,"CrudContratacion/listado.html",{'contratacion':contratacion})




    
def crear_editarContratacion(request,idContratacion=0):
      if request.method=="GET":
        if idContratacion==0:
            formulario=ContratacionForm()   
        else:
            contratacionid=Contratacion.objects.get(pk=idContratacion)
            formulario=ContratacionForm(instance=contratacionid)
        return render(request,'CrudContratacion/Crear.html',{'formulario':formulario})
      else:
        if idContratacion==0:
            formulario=ContratacionForm(request.POST or None, request.FILES or None)
        else:
            contratacionid=Contratacion.objects.get(pk=idContratacion)
            formulario=ContratacionForm(request.POST or None, request.FILES or None ,instance=contratacionid)
        if formulario.is_valid():
            formulario.save()
        return redirect('listaContratacion')
        
def eliminarContratacion(request, idContratacion):
    bc = Contratacion.objects.get(idContratacion=idContratacion)
    bc.delete()
    return redirect('listaContratacion')
        
         
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 
 
 
 
 
 