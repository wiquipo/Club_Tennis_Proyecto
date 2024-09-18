from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import Jugador
from .forms import JugadorForm
from cuota.models import Cuota
from jugadores.models import Jugador
from sociosCuota.models import SocioCuota  # Importar la nueva clase
from django.db.models import Sum

# Create your views here

def listaCuota(request):
    cuotas = Cuota.objects.all()
    total_importe_cuotas = Cuota.objects.aggregate(Sum('importe'))['importe__sum'] or 0  # Sumar el importe de Cuotas
    return render(request, "crudCuotas/listado.html", {'cuotas': cuotas, 'total_importe_cuotas': total_importe_cuotas})

def listaJugador(request):
    jugadores = Jugador.objects.all()
    total_importe_jugadores = Jugador.objects.aggregate(Sum('importe'))['importe__sum'] or 0  # Sumar el importe de Jugadores
    return render(request, "Crud/listado.html", {'jugadores': jugadores, 'total_importe_jugadores': total_importe_jugadores})

def listaSocioCuota(request):
    socios = SocioCuota.objects.all()
    total_importe_socios = SocioCuota.objects.aggregate(Sum('importe'))['importe__sum'] or 0  # Sumar el importe de SocioCuota
    return render(request, "CrudSocioCuotas/listado.html", {'socios': socios, 'total_importe_socios': total_importe_socios})

def sumaTotal(request):
    total_importe_cuotas = Cuota.objects.aggregate(Sum('importe'))['importe__sum'] or 0
    total_importe_jugadores = Jugador.objects.aggregate(Sum('importe'))['importe__sum'] or 0
    total_importe_socios = SocioCuota.objects.aggregate(Sum('importe'))['importe__sum'] or 0
    suma_total = total_importe_cuotas + total_importe_jugadores + total_importe_socios  # Sumar todos los totales
    return render(request, "paginas_base/base.html", {'suma_total': suma_total})

def lista(request):
    jugadores=Jugador.objects.all()
    return render(request,"Crud/listado.html",{'jugadores':jugadores})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarJugador(request,id=0):
      if request.method=="GET":
        if id==0:
            formulario=JugadorForm()   
        else:
            jugadorid=Jugador.objects.get(pk=id)
            formulario=JugadorForm(instance=jugadorid)
        return render(request,'Crud/Crear.html',{'formulario':formulario})
      else:
        if id==0:
            formulario=JugadorForm(request.POST or None, request.FILES or None)
        else:
            jugadorid=Jugador.objects.get(pk=id)
            formulario=JugadorForm(request.POST or None, request.FILES or None ,instance=jugadorid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('lista')
        
def eliminar(request, id):
    bc=Jugador.objects.get(id=id)
    bc.delete()
    return redirect('lista')
        