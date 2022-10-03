from django.db import models
from .usuario import Usuario

class Medico(models.Model): 
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE )
    especialidad = models.CharField(max_length = 30)