# Generated by Django 4.0.3 on 2022-05-16 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opendata', '0014_remove_opendata_content_remove_opendata_content_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opendata',
            name='index',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]