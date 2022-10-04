from rest_framework import serializers
from clinicaBackend.models.usuario import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['rol','nombre','apellido','celular','e_mail','direccion','username','password']