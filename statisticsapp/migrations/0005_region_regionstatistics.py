# Generated by Django 4.0.3 on 2022-04-18 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statisticsapp', '0004_alter_countrystatistics_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('name', models.CharField(choices=[('andijon', 'Andijon viloyati'), ('buxoro', 'Buxoro viloyati'), ('jizzax', 'Jizzax viloyati'), ('qashqadaryo', 'Qashqadaryo viloyati'), ('navoiy', 'Navoiy viloyati'), ('namangan', 'Namangan viloyati'), ('samarqand', 'Samarqand viloyati'), ('surxondaryo', 'Surxondaryo viloyati'), ('sirdaryo', 'Sirdaryo viloyati'), ('toshkent', 'Toshkent viloyati'), ('fargona', 'Fargʻona viloyati'), ('xorazm', 'Xorazm viloyati'), ('qoraqalpogiston', 'Qoraqalpogʻiston Respublikasi'), ('toshkentsh', 'Toshkent shahar')], max_length=100, unique=True, verbose_name='Hududlar')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='RegionStatistics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('count', models.BigIntegerField(verbose_name='Soni')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='statisticsapp.region', verbose_name='Mamlakat')),
                ('science_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='statisticsapp.sciencefield', verbose_name='Yo‘nalish')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mamlakat statistikasi',
                'verbose_name_plural': 'Mamlakat statistikalari',
                'db_table': 'region_statistics',
            },
        ),
    ]
