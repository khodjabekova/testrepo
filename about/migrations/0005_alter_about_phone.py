# Generated by Django 4.0.3 on 2022-05-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_remove_about_history_remove_about_history_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Telefon'),
        ),
    ]
