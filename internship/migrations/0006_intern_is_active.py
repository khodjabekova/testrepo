# Generated by Django 4.0.3 on 2022-04-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0005_alter_intern_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Aktiv'),
        ),
    ]
