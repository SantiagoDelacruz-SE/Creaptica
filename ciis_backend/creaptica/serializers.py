# ciis_backend/creaptica/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PerfilUsuario, Documento

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ['rol']

class UserSerializer(serializers.ModelSerializer):
    perfil_ciis = PerfilUsuarioSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'perfil_ciis']

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__' # Expone todos los campos del modelo