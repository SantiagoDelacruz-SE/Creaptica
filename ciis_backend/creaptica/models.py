from django.db import models
from django.contrib.auth.models import User

# Modelos para perfiles de usuario y roles

class PerfilUsuario(models.Model):
    ROL_CHOICES = [
        ('ADMIN_CIIS', 'Administrador CIIS'),
        ('INVESTIGADOR', 'Investigador'),
        ('DOCENTE', 'Docente'),
        ('ESTUDIANTE', 'Estudiante'),
        # Puedes añadir más roles según las necesidades del CIIS
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_ciis') # related_name para evitar conflictos si tienes otros perfiles
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='ESTUDIANTE', verbose_name="Rol en CIIS")
    # Aquí puedes añadir más campos específicos del perfil, ej:
    # area_investigacion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Área de Investigación")
    # departamento = models.CharField(max_length=100, blank=True, null=True, verbose_name="Departamento")

    def __str__(self):
        return f"{self.usuario.username} - {self.get_rol_display()}"

    class Meta:
        verbose_name = "Perfil de Usuario CIIS"
        verbose_name_plural = "Perfiles de Usuarios CIIS"


# Modelos para la gestion de documentos

class Documento(models.Model):
    ESTADO_CHOICES = [
        ('BORRADOR', 'Borrador'),
        ('EN_REVISION', 'En Revisión'),
        ('PUBLICADO', 'Publicado'),
        ('ARCHIVADO', 'Archivado'),
    ]
    TIPO_DOCUMENTO_CHOICES = [
        ('TESIS', 'Tesis'),
        ('ARTICULO', 'Artículo Científico'),
        ('PONENCIA', 'Ponencia'),
        ('LIBRO', 'Libro'),
        ('CAPITULO_LIBRO', 'Capítulo de Libro'),
        ('INFORME', 'Informe Técnico/Investigación'),
        ('OTRO', 'Otro'),
    ]

    titulo = models.CharField(max_length=255, verbose_name="Título del Documento")
    resumen = models.TextField(blank=True, null=True, verbose_name="Resumen o Descripción")
    archivo = models.FileField(upload_to='documentos_ciis/%Y/%m/%d/', verbose_name="Archivo Adjunto") # Organiza archivos por fecha de subida
    tipo_documento = models.CharField(max_length=30, choices=TIPO_DOCUMENTO_CHOICES, default='OTRO', verbose_name="Tipo de Documento")

    # Relación con el usuario que carga/posee el documento
    # Si usas PerfilUsuario:
    # cargado_por = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='documentos_cargados', verbose_name="Cargado por")
    # Si usas el User de Django directamente:
    autor_principal = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='documentos_creados_ciis', verbose_name="Autor Principal / Cargado por")

    # Para múltiples autores/colaboradores:
    # colaboradores = models.ManyToManyField(User, related_name='documentos_colaborados_ciis', blank=True, verbose_name="Otros Colaboradores")

    palabras_clave = models.CharField(max_length=255, blank=True, null=True, verbose_name="Palabras Clave (separadas por coma)")
    fecha_publicacion = models.DateField(null=True, blank=True, verbose_name="Fecha de Publicación Oficial")
    fecha_carga = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Carga al Sistema")
    ultima_modificacion = models.DateTimeField(auto_now=True, verbose_name="Última Modificación")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='BORRADOR', verbose_name="Estado del Documento")

    # Podrías añadir más campos como:
    # proyecto_investigacion_asociado = models.ForeignKey('ProyectoInvestigacion', on_delete=models.SET_NULL, null=True, blank=True)
    # acceso_restringido = models.BooleanField(default=False, verbose_name="Acceso Restringido")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Documento CIIS"
        verbose_name_plural = "Documentos CIIS"
        ordering = ['-fecha_carga']