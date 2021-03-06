# Generated by Django 4.0.3 on 2022-04-08 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0002_alter_employee_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupervisoryBoard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500, verbose_name='Ismi')),
                ('name_uz', models.CharField(max_length=500, null=True, verbose_name='Ismi')),
                ('name_uzb', models.CharField(max_length=500, null=True, verbose_name='Ismi')),
                ('name_ru', models.CharField(max_length=500, null=True, verbose_name='Ismi')),
                ('name_en', models.CharField(max_length=500, null=True, verbose_name='Ismi')),
                ('position', models.CharField(max_length=500, verbose_name='Lavozimi')),
                ('position_uz', models.CharField(max_length=500, null=True, verbose_name='Lavozimi')),
                ('position_uzb', models.CharField(max_length=500, null=True, verbose_name='Lavozimi')),
                ('position_ru', models.CharField(max_length=500, null=True, verbose_name='Lavozimi')),
                ('position_en', models.CharField(max_length=500, null=True, verbose_name='Lavozimi')),
                ('index', models.IntegerField(blank=True, null=True, verbose_name='Tartib raqami')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Jamg???arma kuzatuv kengashi',
                'verbose_name_plural': 'Jamg???arma kuzatuv kengashlari',
                'db_table': 'supervisory_board',
                'ordering': ['index'],
            },
        ),
    ]
