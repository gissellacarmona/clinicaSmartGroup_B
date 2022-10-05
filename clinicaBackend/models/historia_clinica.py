from django.db import models
from clinicaBackend.models.paciente import Paciente

class Historia_clinica(models.Model): 
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE )
    frec_cardiaca= models.CharField(max_length = 30)
    pres_arterial = models.CharField(max_length = 30)
    temperatura = models.CharField(max_length = 30)
    