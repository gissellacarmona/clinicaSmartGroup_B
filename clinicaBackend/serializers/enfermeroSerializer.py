from rest_framework import serializers
from clinicaBackend.models.enfermero import Enfermero

class EnfermeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermero
        fields = ['usuario','area']