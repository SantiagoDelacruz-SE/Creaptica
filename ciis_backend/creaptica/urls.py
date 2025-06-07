from django.urls import path
from . import views

app_name = 'creaptica' # <--- ¡Importante! Has definido un espacio de nombres para la aplicación.

urlpatterns = [
    # La URL para la vista listar_documentos_json tiene el nombre 'lista_documentos_json_api'
    path('api/documentos_simple/', views.listar_documentos_json, name='lista_documentos_json_api'),
path('api/perfiles_simple/', views.listar_perfiles_json, name='lista_perfiles_json_api_v2'), # o el nombre que prefieras

    # La URL para la vista pagina_inicio_ciis (la que se accede con /ciis/) tiene el nombre 'inicio_creaptica'
    path('', views.pagina_inicio_ciis, name='inicio_creaptica'),
]