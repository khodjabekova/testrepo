# Generated by Django 3.2.4 on 2022-05-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useful_link', '0007_alter_usefullink_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usefullink',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='usefullink',
            name='title_en',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='usefullink',
            name='title_ru',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='usefullink',
            name='title_uz',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AlterField(
            model_name='usefullink',
            name='title_uzb',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Sarlavha'),
        ),
    ]
