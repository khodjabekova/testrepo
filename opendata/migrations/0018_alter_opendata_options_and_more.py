# Generated by Django 4.0.3 on 2022-05-19 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opendata', '0017_alter_opendata_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opendata',
            options={'ordering': ('index',), 'verbose_name': "Ochiq ma'lumot", 'verbose_name_plural': "Ochiq ma'lumotlar"},
        ),
        migrations.AlterModelOptions(
            name='opendataattachments',
            options={'verbose_name': "Ochiq ma'lumot fayllari", 'verbose_name_plural': "Ochiq ma'lumotlar fayllari"},
        ),
        migrations.AlterModelTable(
            name='opendataattachments',
            table='open_data_attachments',
        ),
    ]