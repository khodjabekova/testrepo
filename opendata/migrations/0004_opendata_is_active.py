# Generated by Django 4.0.3 on 2022-04-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opendata', '0003_opendata_title_en_opendata_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opendata',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Aktiv'),
        ),
    ]
