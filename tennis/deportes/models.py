from django.db import models

class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True,verbose_name="idCategoria")
    descripcion=models.CharField(max_length=50,verbose_name="descripcion")
    
    def __str__(self):
      fila=self.descripcion
      return fila
    
# Create your models here.
class DeporteD(models.Model):
    idDeporte = models.AutoField(primary_key=True, db_column='idDeporte')
    nombre=models.CharField(max_length=25,verbose_name="nombre")
    idCategoria=models.ForeignKey(Categoria, verbose_name="idCategoria", on_delete=models.CASCADE)
    horario=models.FloatField(verbose_name="horario")
    
    
    def __str__(self):
        fila=str(self.idDeporte)+"-CÓDIGO CATEGORIA"+str(self.idCategoria)+"-NOMBRE CATEGORIA"+self.nombre
        return fila
    


    
















