# Generated by Django 4.0.3 on 2022-04-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0002_vacancy_body_en_vacancy_body_ru_vacancy_body_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Aktiv'),
        ),
    ]
