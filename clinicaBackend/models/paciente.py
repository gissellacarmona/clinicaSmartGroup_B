from django.db import models
from .usuario import Usuario
from .medico import Medico
from .historia_clinica import Historia_clinica
from .enfermero_paciente import Enfermero_paciente

class Paciente(models.Model): 
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE )
    historia_clinica = models.ForeignKey(Historia_clinica, on_delete=models.CASCADE )
    enfermero_paciente = models.ForeignKey(Enfermero_paciente, on_delete=models.CASCADE )
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE )
    nombreFamiliar= models.CharField(max_length = 30)
    apellidoFamiliar = models.CharField(max_length = 30)
    parentesco = models.CharField(max_length = 30)
    celular = models.CharField(max_length = 30)
