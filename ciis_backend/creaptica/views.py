# Ubicación: ciis_backend/creaptica/views.py
from django.shortcuts import render
from django.http import JsonResponse  # Para devolver respuestas en formato JSON
from .models import Documento, PerfilUsuario  # Importa tus modelos


# Create your views here.

def pagina_inicio_ciis(request):
    # Esta es una vista simple que podría renderizar una plantilla HTML más adelante
    # Por ahora, solo devolvemos un mensaje simple.
    contexto = {
        'mensaje': 'Bienvenido a la infraestructura digital del CIIS (Backend)',
        'numero_documentos': Documento.objects.count(),  # Cuenta cuántos documentos hay
        'numero_usuarios_perfil': PerfilUsuario.objects.count()  # Cuenta cuántos perfiles hay
    }
    return render(request, 'ciis_app/pagina_inicio.html', contexto)  # Necesitarás crear esta plantilla


def listar_documentos_json(request):
    documentos = Documento.objects.all()  # Obtiene todos los objetos Documento

    # Preparamos los datos para convertirlos a JSON
    # Esto es una forma manual, más adelante usaremos serializers con DRF para esto
    data_documentos = []
    for doc in documentos:
        data_documentos.append({
            'id': doc.id,
            'titulo': doc.titulo,
            'tipo_documento_display': doc.get_tipo_documento_display(),  # Muestra el nombre legible del choice
            'autor_principal_username': doc.autor_principal.username if doc.autor_principal else "N/A",
        })

    return JsonResponse(data_documentos, safe=False, json_dumps_params={'ensure_ascii': False})


def listar_perfiles_json(request):
    perfiles = PerfilUsuario.objects.all()
    data_perfiles = []
    for perfil in perfiles:
        data_perfiles.append({
            'id_usuario': perfil.usuario.id,
            'nombre_usuario': perfil.usuario.username,
            'rol_ciis': perfil.get_rol_display(),
            'email': perfil.usuario.email
        })
    return JsonResponse({'perfiles_usuarios': data_perfiles}, json_dumps_params={'ensure_ascii': False})