from socket import fromshare
from django import forms 
from .models import Socio

class SocioForm(forms.ModelForm):
  class Meta:
        model=Socio
       #fields='__all__'
        fields=('DNI','nom','fechan',"dire","cp","tel")
        labels ={
            "DNI" : "DNI del socio" ,
            'nom': 'nombre y apellido del socio:',
            "fechan" : "fecha de nacimiento del socio MES/DÍA/AÑO" ,
            "dire" : "direccion del socio",
            "cp" : "codigo postal del socio",
            "tel":"Telefono",
                      #  "nummac" : "numero de macc " ,
                   
        }
        
    
  def __init__(self, *args, **kwargs):
        super(SocioForm,self).__init__(*args,**kwargs)
     #   self.fields['nom'].empty_label="Selecciona"
        self.fields['nom'].required=True
        self.fields['fechan'].required=False
        