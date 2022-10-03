from django.db import models
from .enfermero import Enfermero
from .paciente import Paciente

class Enfermero_paciente(models.Model): 
    id = models.AutoField(primary_key=True)
    enfermero = models.ForeignKey(Enfermero, on_delete=models.CASCADE )
    paciente = models.ForeignKey(Paci, on_delete=models.CASCADE )