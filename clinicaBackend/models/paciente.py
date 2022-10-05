from django.db import models
from .usuario import Usuario
from .medico import Medico
from .enfermero import Enfermero

class Paciente(models.Model): 
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE )
    enfermero = models.ForeignKey(Enfermero, on_delete=models.CASCADE, null=True )
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=True )
    nombreFamiliar= models.CharField(max_length = 30)
    apellidoFamiliar = models.CharField(max_length = 30)
    parentesco = models.CharField(max_length = 30)
    celular = models.CharField(max_length = 30)