from dataclasses import fields
from rest_framework import serializers
from clinicaBackend.models.paciente import Paciente

class Asignar_med_enfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id','medico','enfermero']