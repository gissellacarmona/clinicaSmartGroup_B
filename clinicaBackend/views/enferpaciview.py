from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from clinicaBackend.serializers.enferpaciSerializer import EnferpaciSerializer
from clinicaBackend.serializers.usuarioSerializer import UsuarioSerializer
from clinicaBackend.models.enfermero_paciente import Enfermero_paciente

class EnferpaciListView(generics.ListCreateAPIView):
    queryset = Enfermero_paciente.objects.all()
    serializer_class = EnferpaciSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los Enfermeros/pacientes")
        queryset = self.get_queryset()
        serializer = EnferpaciSerializer(queryset, many=True)
        return Response(serializer.data)

        """ tokenData = {
                     "username":request.data["username"],
                     "password":request.data["password"]
                    }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) """
