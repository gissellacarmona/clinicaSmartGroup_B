from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from clinicaBackend.serializers.histclinSerializer import HistclinSerializer
from clinicaBackend.serializers.usuarioSerializer import UsuarioSerializer
from clinicaBackend.models.historia_clinica import Historia_clinica

class HistclinListCreateView(generics.ListCreateAPIView):
    queryset = Historia_clinica.objects.all()
    serializer_class = HistclinSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos las Historias clinicas")
        queryset = self.get_queryset()
        serializer = HistclinSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Historia_clinica")
        usuarioData = request.data.pop('usuario')
        serializerU  = UsuarioSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        enfData = request.data   
        enfData.update({"usuario":usuario.id})
        serializerEnf = HistclinSerializer(data=enfData)
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()
        return Response(status=status.HTTP_201_CREATED)

        """ tokenData = {
                     "username":request.data["username"],
                     "password":request.data["password"]
                    }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) """

class HistclinRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Historia_clinica.objects.all()
    serializer_class = HistclinSerializer
    lookup_field = "id"             # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Historia_clinica")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Historia_clinica")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().put(request, *args, **kwargs)