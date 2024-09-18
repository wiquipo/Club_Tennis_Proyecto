from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import SocioCuota
from .forms import SocioCuotaForm
from cuota.models import Cuota
from jugadores.models import Jugador
from sociosCuota.models import SocioCuota  # Importar la nueva clase
from django.db.models import Sum
# Create your views here

def listaCuota(request):
    cuotas = Cuota.objects.all()
    total_importe_cuotas = Cuota.objects.aggregate(Sum('importe'))['importe__sum'] or 0  # Sumar el importe de Cuotas
    return render(request, "Crud/listado.html", {'cuotas': cuotas, 'total_importe_cuotas': total_importe_cuotas})

def listaJugador(request):
    jugadores = Jugador.objects.all()
    total_importe_jugadores = Jugador.objects.aggregate(Sum('importe'))['importe__sum'] or 0  # Sumar el importe de Jugadores
    return render(request, "crudCuota/listado.html", {'jugadores': jugadores, 'total_importe_jugadores': total_importe_jugadores})

def listaSocioCuota(request):
    socios = SocioCuota.objects.all()
    total_importe_socios = SocioCuota.objects.aggregate(Sum('imp'))['imp__sum'] or 0  # Sumar el importe de SocioCuota
    return render(request, "CrudSocioCuota/listado.html", {'socios': socios, 'total_importe_socios': total_importe_socios})

def sumaTotal(request):
    total_importe_cuotas = Cuota.objects.aggregate(Sum('importe'))['importe__sum'] or 0
    total_importe_socios = SocioCuota.objects.aggregate(Sum('importe'))['importe__sum'] or 0
    
    # Sumar los importes de Cuotas y Socios
    suma_total = total_importe_cuotas + total_importe_socios
    print(f"Suma total: {suma_total}")  # Para depuración
    
    return render(request, "sumaTotal.html", {'suma_total': suma_total})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarSocioCuota(request,id=0):
      if request.method=="GET":
        if id==0:
            formulario=SocioCuotaForm()   
        else:
            Socioid=SocioCuota.objects.get(pk=id)
            formulario=SocioCuotaForm(instance=Socioid)
        return render(request,'CrudSocioCuota/Crear.html',{'formulario':formulario})
      else:
        if id==0:
            formulario=SocioCuotaForm(request.POST or None, request.FILES or None)
        else:
            Socioid=SocioCuota.objects.get(pk=id)
            formulario=SocioCuotaForm(request.POST or None, request.FILES or None ,instance=Socioid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaSocioCuota')
        
def eliminar(request, id):
    bc=SocioCuota.objects.get(id=id)
    bc.delete()
    return redirect('listaSocioCuota')
        