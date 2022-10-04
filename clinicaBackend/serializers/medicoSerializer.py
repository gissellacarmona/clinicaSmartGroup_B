from rest_framework import serializers
from clinicaBackend.models.medico import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['usuario','especialidad']