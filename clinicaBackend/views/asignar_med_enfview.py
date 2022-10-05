from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from clinicaBackend.serializers.asignar_med_enfserializer import Asignar_med_enfSerializer
from clinicaBackend.models.paciente import Paciente

class Asignar_med_enfviewListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = Asignar_med_enfSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET las asignaciones a los Pacientes")
        queryset = self.get_queryset()
        serializer = Asignar_med_enfSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a asignar Medico y Enfermero a Paciente")
        pacienteData = request.data.pop('paciente')
        serializerU  = Asignar_med_enfSerializer(data=pacienteData)
        serializerU.is_valid(raise_exception=True)
        serializerU.save()