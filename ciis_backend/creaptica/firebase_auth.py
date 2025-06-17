# ciis_backend/creaptica/firebase_auth.py
import os
import firebase_admin
from firebase_admin import credentials, auth
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from .models import PerfilUsuario

# Inicializa Firebase Admin SDK usando la ruta del archivo de credenciales
try:
    cred = credentials.Certificate(os.path.join(settings.BASE_DIR, 'creaptica-ciis-firebase-adminsdk-fbsvc-c592f94d6a.json'))
    firebase_admin.initialize_app(cred)
except Exception as e:
    print(f"Error inicializando Firebase: {e}")

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            # Nadie está intentando autenticarse
            return None

        # El token debe venir como "Bearer <token>"
        token_parts = auth_header.split(" ")
        if len(token_parts) != 2 or token_parts[0].lower() != "bearer":
            # Formato de header inválido
            return None

        id_token = token_parts[1]
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            # El token es inválido o ha expirado
            raise exceptions.AuthenticationFailed('Token inválido o expirado.')

        # Obtenemos el email del token verificado
        email = decoded_token.get('email')
        if not email:
            raise exceptions.AuthenticationFailed('El token no contiene un email.')

        # Creamos o buscamos al usuario en la base de datos de Django
        # Esto nos permite usar el sistema de permisos de Django/DRF
        user, created = User.objects.get_or_create(
            email=email,
            defaults={'username': email} # Usamos el email como username por simplicidad
        )

        # Si el usuario es nuevo, le asignamos un perfil por defecto
        if created:
            PerfilUsuario.objects.create(usuario=user, rol='ESTUDIANTE') # Rol por defecto

        return (user, None)