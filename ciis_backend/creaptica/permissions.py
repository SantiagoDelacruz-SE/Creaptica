# ciis_backend/creaptica/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS


# Permiso para el Admin: acceso total
class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.perfil_ciis.rol == 'ADMIN_CIIS'


# Permiso para el Investigador: puede leer y crear, pero no modificar/eliminar
class IsInvestigador(BasePermission):
    def has_permission(self, request, view):
        if not (request.user.is_authenticated and hasattr(request.user, 'perfil_ciis')):
            return False

        is_investigador = request.user.perfil_ciis.rol == 'INVESTIGADOR'

        # Si es investigador, puede leer (GET, HEAD, OPTIONS) y crear (POST)
        if is_investigador and (request.method in SAFE_METHODS or request.method == 'POST'):
            return True

        return False


# Permiso para Docentes y Estudiantes: solo pueden leer
class IsDocenteOrEstudianteReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not (request.user.is_authenticated and hasattr(request.user, 'perfil_ciis')):
            return False

        rol = request.user.perfil_ciis.rol
        is_allowed_role = rol in ['DOCENTE', 'ESTUDIANTE']

        # Solo permite métodos seguros (GET, HEAD, OPTIONS)
        return is_allowed_role and request.method in SAFE_METHODS