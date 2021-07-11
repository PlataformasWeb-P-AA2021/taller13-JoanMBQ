from django.db import models

# Create your models here.
class Edificio(models.Model):
    opciones_edifico = (
        ('residencial', 'Residencial'),
        ('rural', 'Rural')
    )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField("Tipo Edificio",max_length=30, \
            choices=opciones_edifico) 

    def __str__(self):
        return "%s - %s - %s - %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

    def obtener_costo_departamentos(self):
        valor = [d.costo for d in self.departamentos.all()]
        valor = sum(valor)
        return valor
    
    def obtener_total_cuartos(self):
        valor = [d.num_cuartos for d in self.departamentos.all()]
        valor = sum(valor)
        return valor

class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=100, decimal_places=2)
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s - %s - %s" % (self.nombre_propietario, self.costo,\
        self.num_cuartos)