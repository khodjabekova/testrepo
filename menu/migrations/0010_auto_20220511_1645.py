# Generated by Django 3.2.4 on 2022-05-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_alter_menu_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='note',
            field=models.TextField(blank=True, max_length=2500, null=True, verbose_name='Izoh'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='note_en',
            field=models.TextField(blank=True, max_length=2500, null=True, verbose_name='Izoh'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='note_ru',
            field=models.TextField(blank=True, max_length=2500, null=True, verbose_name='Izoh'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='note_uz',
            field=models.TextField(blank=True, max_length=2500, null=True, verbose_name='Izoh'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='note_uzb',
            field=models.TextField(blank=True, max_length=2500, null=True, verbose_name='Izoh'),
        ),
    ]
