from django.db import models

from jugadores.models import Deporte

# Create your models here.
class Profesor(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    DNI=models.IntegerField(verbose_name="DNI")
    nom = models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    fechan=models.DateField(verbose_name="Fecha Nacimiento")
    dire=models.CharField(max_length=50,verbose_name="Direccion")
    cd=models.CharField(max_length=6,verbose_name="codigo postal")
    descripcion=models.ForeignKey(Deporte, max_length=50,verbose_name="descripcion", on_delete=models.CASCADE)
    
    
    def __str__(self):
        fila=str(self.id)+"-"+str(self.DNI)+"-"+self.nom
        return fila
    


    
















