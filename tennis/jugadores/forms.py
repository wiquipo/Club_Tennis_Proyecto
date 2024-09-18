from socket import fromshare
from django import forms 
from .models import Jugador

class JugadorForm(forms.ModelForm):
  class Meta:
        model=Jugador
       #fields='__all__'
        fields=('DNI','nom','fechan','altura',"peso","dire","cd","talla","descripcion")
        labels ={
            "DNI" : "DNI" ,
            'nom': 'nombre y apellido',
            "fechan" : "Fecha de nacimiento MES/DÍA/AÑO" ,
            "altura" : "Altura" ,
            "peso" : "Peso" , 
            "dire" : "Direccion",
            "cd" : "Código postal",
            "talla" : "Talla de indumentaria ",
            "descripcion" : "Deporte al que pertenece",
          #  "nummac" : "numero de macc " ,
           
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(JugadorForm,self).__init__(*args,**kwargs)
        self.fields['descripcion'].empty_label="Selecciona"
        self.fields['nom'].required=True
        self.fields['fechan'].required=False
        