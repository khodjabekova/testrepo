# Generated by Django 4.0.3 on 2022-05-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_alter_contact_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=1200, verbose_name='Xabar'),
        ),
    ]
