from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import DeporteD
from .forms import DeporteDForm


# Create your views here

def listaD(request):
    deporte=DeporteD.objects.all()
    return render(request,"CrudDeporte/listado.html",{'deportes':deporte})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')  
      
def crear_editarDeporteD(request, idDeporte=0):
    if request.method == "GET":
        if idDeporte == 0:
            formulario = DeporteDForm()
        else:
            deporteid = DeporteD.objects.get(pk=idDeporte)
            formulario = DeporteDForm(instance=deporteid)
        return render(request, 'CrudDeporte/Crear.html', {'formulario': formulario})
    else:
        if idDeporte == 0:
            formulario = DeporteDForm(request.POST or None, request.FILES or None)
        else:
            deporteid = DeporteD.objects.get(pk=idDeporte)
            formulario = DeporteDForm(request.POST or None, request.FILES or None, instance=deporteid)
        if formulario.is_valid():
            formulario.save()
        return redirect('listaD')


       
def eliminarD (request, idDeporte):
    bc=DeporteD.objects.get(pk=idDeporte)
    bc.delete()
    return redirect('listaD')
        