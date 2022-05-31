# Generated by Django 4.0.3 on 2022-05-06 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opendata', '0009_opendata_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='opendata',
            name='content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Matni'),
        ),
        migrations.AddField(
            model_name='opendata',
            name='content_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Matni'),
        ),
        migrations.AddField(
            model_name='opendata',
            name='content_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Matni'),
        ),
        migrations.AddField(
            model_name='opendata',
            name='content_uzb',
            field=models.TextField(blank=True, null=True, verbose_name='Matni'),
        ),
    ]
