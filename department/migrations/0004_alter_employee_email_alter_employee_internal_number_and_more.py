# Generated by Django 4.0.3 on 2022-04-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_supervisoryboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='internal_number',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Ichki raqami'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Telefon raqami'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='employee', verbose_name='Rasm'),
        ),
    ]
