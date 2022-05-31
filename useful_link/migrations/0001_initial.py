# Generated by Django 4.0.3 on 2022-03-30 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import useful_link.validation
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsefulLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Title')),
                ('url', models.URLField(blank=True, max_length=500, null=True, verbose_name='Havola')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/usefullink', validators=[useful_link.validation.file_validation_exception], verbose_name='Rasm')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Foydali havola',
                'verbose_name_plural': 'Foydali havolalar',
                'db_table': 'useful_link',
            },
        ),
    ]