from django.db import models

class Especialidad(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nombre


class Tipo(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='tipos')

    def __str__(self):
        return self.nombre
    
class Conmorbilidad(models.Model):
    asa1 = models.CharField(max_length=250)
    asa2 = models.CharField(max_length=250)
    asa3 = models.CharField(max_length=250)
    asa4 = models.CharField(max_length=250)
        
class Ingreso(models.Model):
    edad = models.CharField(max_length=3)
    especialidad = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='tipos')
    asa = models.ForeignKey(Conmorbilidad, on_delete=models.CASCADE, related_name='ingresos')

    def __str__(self):
        return f"Ingreso: {self.edad} - {self.especialidad}"
    
    

        
        



