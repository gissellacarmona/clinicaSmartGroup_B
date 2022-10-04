from rest_framework import serializers
from clinicaBackend.models.historia_clinica import Historia_clinica

class HistclinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia_clinica
        fields = ['frec_cardiaca','pres_arterial','temperatura']