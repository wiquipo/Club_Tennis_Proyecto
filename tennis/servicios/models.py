from django.db import models


    
# Create your models here.
class Servicio(models.Model):
    idServicio = models.AutoField(primary_key=True, db_column='Código del Servicio')
    descripcion=models.TextField(verbose_name="Descripción del Servicio")
    costo= models.FloatField(max_length=50,verbose_name="Costo del Servicio")
          
    
    def __str__(self):
        fila=str(self.idServicio)+"-"+self.descripcion+"-"+str(self.costo)
        return fila
    
    
# Create your models here.
class Contratacion(models.Model):
    idContratacion = models.AutoField(primary_key=True, db_column='idContratacion')
    fecha=models.DateField(verbose_name="fecha")
    idServicio= models.ForeignKey(Servicio,verbose_name="idServicio",on_delete=models.CASCADE)
    nomContratante=models.TextField(max_length=25,verbose_name="nomContratante")
    
       
    def __str__(self):
        fila=str(self.idContratacion)+"-"+self.fecha+"-"+self.nomContaratante
        return fila
    

    