from socket import fromshare
from django import forms 
from .models import Profesor

class ProfesorForm(forms.ModelForm):
  class Meta:
        model=Profesor
       #fields='__all__'
        fields=('DNI','nom','fechan',"dire","cd","descripcion")
        labels ={
            "DNI" : "DNI" ,
            'nom': 'nombre y apellido',
            "fechan" : "Fecha de nacimiento MES/DÍA/AÑO" ,
            "dire" : "Direccion",
            "cd" : "Código postal",
            "descripcion" : "Deporte al que pertenece",
          #  "nummac" : "numero de macc " ,
           
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(ProfesorForm,self).__init__(*args,**kwargs)
        self.fields['descripcion'].empty_label="Selecciona"
        self.fields['nom'].required=True
        self.fields['fechan'].required=False
        