# Generated by Django 4.0.3 on 2022-04-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='body_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='body_uz',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='body_uzb',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='title_uzb',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
    ]
