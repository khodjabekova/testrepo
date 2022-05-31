# Generated by Django 4.0.3 on 2022-04-04 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500, verbose_name='Boʻlim nomi')),
                ('name_uz', models.CharField(max_length=500, null=True, verbose_name='Boʻlim nomi')),
                ('name_uzb', models.CharField(max_length=500, null=True, verbose_name='Boʻlim nomi')),
                ('name_ru', models.CharField(max_length=500, null=True, verbose_name='Boʻlim nomi')),
                ('name_en', models.CharField(max_length=500, null=True, verbose_name='Boʻlim nomi')),
                ('index', models.IntegerField(blank=True, null=True, verbose_name='Tartib raqami')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_departments', to='department.department', verbose_name='Yuqori boʻlim')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Boʻlim',
                'verbose_name_plural': 'Boʻlimlar',
                'db_table': 'department',
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, verbose_name='Toʻliq ismi')),
                ('name_uz', models.CharField(max_length=250, null=True, verbose_name='Toʻliq ismi')),
                ('name_uzb', models.CharField(max_length=250, null=True, verbose_name='Toʻliq ismi')),
                ('name_ru', models.CharField(max_length=250, null=True, verbose_name='Toʻliq ismi')),
                ('name_en', models.CharField(max_length=250, null=True, verbose_name='Toʻliq ismi')),
                ('email', models.CharField(max_length=250, null=True, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=250, null=True, verbose_name='Telefon raqami')),
                ('internal_number', models.CharField(max_length=250, null=True, verbose_name='Ichki raqami')),
                ('position', models.CharField(max_length=250, null=True, verbose_name='Lavozimi')),
                ('position_uz', models.CharField(max_length=250, null=True, verbose_name='Lavozimi')),
                ('position_uzb', models.CharField(max_length=250, null=True, verbose_name='Lavozimi')),
                ('position_ru', models.CharField(max_length=250, null=True, verbose_name='Lavozimi')),
                ('position_en', models.CharField(max_length=250, null=True, verbose_name='Lavozimi')),
                ('is_chief', models.BooleanField(default=False, verbose_name='Boʻlim boshligʻi')),
                ('photo', models.ImageField(null=True, upload_to='employee', verbose_name='Rasm')),
                ('biography', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Tarjimai holi')),
                ('biography_uz', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Tarjimai holi')),
                ('biography_uzb', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Tarjimai holi')),
                ('biography_ru', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Tarjimai holi')),
                ('biography_en', models.TextField(blank=True, max_length=1500, null=True, verbose_name='Tarjimai holi')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department', verbose_name='Boʻlim')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Hodim',
                'verbose_name_plural': 'Hodimlar',
                'db_table': 'employee',
            },
        ),
    ]
