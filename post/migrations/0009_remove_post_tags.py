# Generated by Django 4.0.3 on 2022-05-19 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20220511_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]