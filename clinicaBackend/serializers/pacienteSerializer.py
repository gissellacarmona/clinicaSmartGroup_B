from rest_framework import serializers
from clinicaBackend.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['usuario','historia_clinica', 'medico','nombreFamiliar','apellidoFamiliar','parentesco','celular']