# Generated by Django 4.0.3 on 2022-05-17 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_alter_videogallery_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photogallery',
            options={'ordering': ['-index'], 'verbose_name': 'Foto galereya', 'verbose_name_plural': 'Foto galereya'},
        ),
        migrations.AlterModelOptions(
            name='videogallery',
            options={'ordering': ['-index'], 'verbose_name': 'Video galereya', 'verbose_name_plural': 'Video galereya'},
        ),
    ]