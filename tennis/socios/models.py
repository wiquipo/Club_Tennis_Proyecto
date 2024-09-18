from django.db import models


    
# Create your models here.
class Socio(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    DNI=models.IntegerField(verbose_name="DNI")
    nom = models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    fechan=models.DateField(verbose_name="Fecha Nacimiento")
    dire=models.CharField(max_length=50,verbose_name="Direccion")
    cp=models.CharField(max_length=6,verbose_name="codigo postal")
    tel=models.CharField(max_length=15,verbose_name="telefono")
 
    
    
    def __str__(self):
        fila=str(self.id)+"-"+str(self.DNI)+"-"+self.nom
        return fila
    


    