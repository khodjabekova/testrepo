# Generated by Django 4.0.3 on 2022-04-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0009_remove_intern_internship_remove_intern_internship_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='phone',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Telefon'),
        ),
    ]
