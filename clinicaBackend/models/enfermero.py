from django.db import models
from .usuario import Usuario

class Enfermero(models.Model): 
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE )
    area = models.CharField(max_length = 30)