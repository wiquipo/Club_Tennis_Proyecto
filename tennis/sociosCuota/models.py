from django.db import models


    
# Create your models here.
class SocioCuota(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    DNI=models.IntegerField(verbose_name="DNI")
    nom = models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    fechaMes=models.DateField(verbose_name="Fecha Mes a abonar")
    fechap=models.DateField(verbose_name="Fecha pago")
    tel=models.CharField(max_length=15,verbose_name="telefono")
    imp=models.FloatField(verbose_name="importe")
 
 
 
 
 
 
    
    
    def __str__(self):
        fila=str(self.id)+"-"+str(self.DNI)+"-"+self.nom
        return fila
    


    