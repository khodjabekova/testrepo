# Generated by Django 4.0.3 on 2022-04-21 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='transport_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Transport'),
        ),
        migrations.AddField(
            model_name='about',
            name='transport_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Transport'),
        ),
        migrations.AddField(
            model_name='about',
            name='transport_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Transport'),
        ),
        migrations.AddField(
            model_name='about',
            name='transport_uzb',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Transport'),
        ),
    ]