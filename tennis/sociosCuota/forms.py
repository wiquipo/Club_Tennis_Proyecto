from socket import fromshare
from django import forms 
from .models import SocioCuota

class SocioCuotaForm(forms.ModelForm):
  class Meta:
        model=SocioCuota
       #fields='__all__'
        fields=('DNI','nom','fechaMes',"fechap","tel","imp")

        labels ={
            "DNI" : "DNI del socio" ,
            'nom': 'Nombre y apellido del socio:',
            "fechaMes" : "Fecha Mes a Abonar cuota socio" ,
            "fechap" : "Fecha pago",
            "tel" : "Telefono",
            "imp":"Importe",
            
          #  "nummac" : "numero de macc " ,
           
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(SocioCuotaForm,self).__init__(*args,**kwargs)
        self.fields['DNI'].empty_label="Selecciona"
        self.fields['nom'].required=True
        self.fields['fechaMes'].required=False
        