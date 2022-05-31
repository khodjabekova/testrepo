# Generated by Django 4.0.3 on 2022-04-12 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0005_department_is_active_employee_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Aktiv'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Aktiv'),
        ),
        migrations.AlterField(
            model_name='supervisoryboard',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Aktiv'),
        ),
    ]
