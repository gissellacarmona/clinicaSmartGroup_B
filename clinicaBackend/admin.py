from django.contrib import admin
from .models.usuario import Usuario
from .models.medico import Medico
from .models.paciente import Paciente
from .models.historia_clinica import Historia_clinica
from .models.enfermero import Enfermero

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Historia_clinica)
admin.site.register(Enfermero)

