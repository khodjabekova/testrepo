# Generated by Django 4.0.3 on 2022-04-14 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0005_alter_vacancy_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Havola'),
        ),
    ]