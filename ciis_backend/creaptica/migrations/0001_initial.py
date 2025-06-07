import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título del Documento')),
                ('resumen', models.TextField(blank=True, null=True, verbose_name='Resumen o Descripción')),
                ('archivo', models.FileField(upload_to='documentos_ciis/%Y/%m/%d/', verbose_name='Archivo Adjunto')),
                ('tipo_documento', models.CharField(choices=[('TESIS', 'Tesis'), ('ARTICULO', 'Artículo Científico'), ('PONENCIA', 'Ponencia'), ('LIBRO', 'Libro'), ('CAPITULO_LIBRO', 'Capítulo de Libro'), ('INFORME', 'Informe Técnico/Investigación'), ('OTRO', 'Otro')], default='OTRO', max_length=30, verbose_name='Tipo de Documento')),
                ('palabras_clave', models.CharField(blank=True, max_length=255, null=True, verbose_name='Palabras Clave (separadas por coma)')),
                ('fecha_publicacion', models.DateField(blank=True, null=True, verbose_name='Fecha de Publicación Oficial')),
                ('fecha_carga', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga al Sistema')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True, verbose_name='Última Modificación')),
                ('estado', models.CharField(choices=[('BORRADOR', 'Borrador'), ('EN_REVISION', 'En Revisión'), ('PUBLICADO', 'Publicado'), ('ARCHIVADO', 'Archivado')], default='BORRADOR', max_length=20, verbose_name='Estado del Documento')),
                ('autor_principal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documentos_creados_ciis', to=settings.AUTH_USER_MODEL, verbose_name='Autor Principal / Cargado por')),
            ],
            options={
                'verbose_name': 'Documento CIIS',
                'verbose_name_plural': 'Documentos CIIS',
                'ordering': ['-fecha_carga'],
            },
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('ADMIN_CIIS', 'Administrador CIIS'), ('INVESTIGADOR', 'Investigador'), ('DOCENTE', 'Docente'), ('ESTUDIANTE', 'Estudiante')], default='ESTUDIANTE', max_length=20, verbose_name='Rol en CIIS')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_ciis', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de Usuario CIIS',
                'verbose_name_plural': 'Perfiles de Usuarios CIIS',
            },
        ),
    ]
