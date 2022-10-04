from rest_framework import serializers
from clinicaBackend.models.enfermero_paciente import Enfermero_paciente

class EnferpaciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero_paciente
        fields = ['enfermero','paciente']