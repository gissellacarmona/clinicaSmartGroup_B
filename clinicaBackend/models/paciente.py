from django.db import models
from .usuario import Usuario
from .medico import Medico

class Paciente(models.Model): 
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, related_name='paciente', on_delete=models.CASCADE )
    medico = models.ForeignKey(Medico, related_name='paciente', on_delete=models.CASCADE )
    nombreFamiliar= models.CharField('Nombre Familiar', max_length = 30)
    apellidoFamiliar = models.CharField('Apellido familiar', max_length = 30)
    parentesco = models.CharField('Parentesco', max_length = 30)
    celular = models.CharField('Celular', max_length = 30)
