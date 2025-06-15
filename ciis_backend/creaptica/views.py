# ciis_backend/creaptica/views.py
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Documento
from .serializers import DocumentoSerializer, UserSerializer
from .permissions import IsAdmin, IsInvestigador, IsDocenteOrEstudianteReadOnly

# ViewSet para el modelo Documento
# Provee automáticamente las acciones: list, create, retrieve, update, destroy
class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    # Un usuario debe cumplir al menos una de estas políticas de permisos
    permission_classes = [IsAdmin | IsInvestigador | IsDocenteOrEstudianteReadOnly]

# Una vista simple para que el usuario autenticado pueda obtener su propio perfil y rol
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)