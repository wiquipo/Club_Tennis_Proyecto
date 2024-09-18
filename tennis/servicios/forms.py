from socket import fromshare
from django import forms 
from .models import Servicio, Contratacion

class ServicioForm(forms.ModelForm):
  class Meta:
        model=Servicio
       #fields='__all__'
        fields=('descripcion','costo')
        labels ={
            
            'descripcion': 'Descripción:',
            "costo" : "Costo" ,
                              
        }
        
    
  def __init__(self, *args, **kwargs):
        super(ServicioForm,self).__init__(*args,**kwargs)
        self.fields['descripcion'].empty_label="Selecciona"
        self.fields['descripcion'].required=True
        self.fields['costo'].required=False
        
        

class ContratacionForm(forms.ModelForm):
  class Meta:
        model=Contratacion
       #fields='__all__'
        fields=('fecha','idServicio','nomContratante')
        labels ={
            
            'fecha': 'Fecha contratación:',
            "idServicio" : "Cód de Servicio" ,
            'nomContratante':'Nombre del Contratante',
                              
        }
        
    
  def __init__(self, *args, **kwargs):
        super(ContratacionForm,self).__init__(*args,**kwargs)
     #   self.fields['nom'].empty_label="Selecciona"
        self.fields['idServicio'].required=True
        self.fields['fecha'].required=True
        self.fields['nomContratante'].required=False        
        