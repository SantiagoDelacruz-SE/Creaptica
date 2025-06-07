from django.contrib import admin
from .models import PerfilUsuario, Documento # Importa tus modelos

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol', 'get_user_email') # Muestra estos campos en la lista
    list_filter = ('rol',) # Permite filtrar por rol
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name', 'usuario__email') # Campos para búsqueda

    @admin.display(description='Email del Usuario')
    def get_user_email(self, obj):
        return obj.usuario.email

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_documento', 'autor_principal', 'fecha_carga', 'estado')
    list_filter = ('tipo_documento', 'estado', 'fecha_publicacion')
    search_fields = ('titulo', 'resumen', 'palabras_clave', 'autor_principal__username')
    date_hierarchy = 'fecha_carga' # Navegación por fechas
    # Para campos de solo lectura en el admin:
    # readonly_fields = ('fecha_carga', 'ultima_modificacion')
    fieldsets = (
        (None, {
            'fields': ('titulo', 'resumen', 'archivo')
        }),
        ('Detalles y Clasificación', {
            'fields': ('tipo_documento', 'autor_principal', 'palabras_clave', 'estado') # 'colaboradores' si lo añades
        }),
        ('Fechas Importantes', {
            'fields': ('fecha_publicacion', 'fecha_carga', 'ultima_modificacion'),
            'classes': ('collapse',) # Para que esta sección aparezca colapsada
        }),
    )
    # Asegúrate de que los campos readonly estén en fieldsets o no sean editables
    readonly_fields = ('fecha_carga', 'ultima_modificacion')