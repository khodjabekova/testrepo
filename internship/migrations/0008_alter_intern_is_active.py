# Generated by Django 4.0.3 on 2022-04-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0007_alter_intern_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Aktiv'),
        ),
    ]
