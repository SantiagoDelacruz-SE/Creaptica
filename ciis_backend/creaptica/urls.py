# ciis_backend/creaptica/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentoViewSet, UserProfileView

# El router genera automáticamente las URLs para el ViewSet (GET, POST, PUT, DELETE)
router = DefaultRouter()
router.register(r'documentos', DocumentoViewSet, basename='documento')

urlpatterns = [
    # Ruta para obtener el perfil del usuario actual: /api/profile/
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    # Incluye las URLs generadas por el router: /api/documentos/
    path('', include(router.urls)),
]