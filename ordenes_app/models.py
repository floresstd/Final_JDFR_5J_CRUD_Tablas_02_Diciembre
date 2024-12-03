from django.db import models

class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True) 
    Id_cliente = models.IntegerField()
    Fecha = models.DateField(null=True, blank=True)
    Id_producto = models.IntegerField()
    Id_Categoria = models.IntegerField()
    Cantidad = models.IntegerField()
    

    def __str__(self):
        return self.id_orden