from django.shortcuts import render, redirect
from django.http import HttpResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .forms import CuotaForm
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
    return render(request, "crudCuotas/listado.html", {'jugadores': jugadores, 'total_importe_jugadores': total_importe_jugadores})

def listaSocioCuota(request):
    socios = SocioCuota.objects.all()
    total_importe_socios = SocioCuota.objects.aggregate(Sum('importe'))['importe__sum'] or 0  # Sumar el importe de SocioCuota
    return render(request, "crudSocioCuotas/listado.html", {'socios': socios, 'total_importe_socios': total_importe_socios})

def sumaTotal(request):
    total_importe_cuotas = Cuota.objects.aggregate(Sum('importe'))['importe__sum'] or 0
    # total_importe_jugadores = Jugador.objects.aggregate(Sum('importe'))['importe__sum'] or 0
    total_importe_socios = SocioCuota.objects.aggregate(Sum('imp'))['imp__sum'] or 0
    suma_total = total_importe_cuotas + total_importe_socios  # Sumar todos los totales
    return render(request, "paginas_base/inicio.html", {'suma_total': suma_total})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarCuota(request,idCuota=0):
      if request.method=="GET":
        if idCuota==0:
            formulario=CuotaForm()   
        else:
            cuotaid=Cuota.objects.get(pk=idCuota)
            formulario=CuotaForm(instance=cuotaid)
        return render(request,'crudCuotas/Crear.html',{'formulario':formulario})
      else:
        if idCuota==0:
            formulario=CuotaForm(request.POST or None, request.FILES or None)
        else:
            cuotaid=Cuota.objects.get(pk=idCuota)
            formulario=CuotaForm(request.POST or None, request.FILES or None ,instance=cuotaid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaCuota')
        
def eliminaCuota(request, idCuota):
    bc=Cuota.objects.get(pk=idCuota)
    bc.delete()
    return redirect('listaCuota')
