# Generated by Django 4.0.3 on 2022-05-26 14:41

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_alter_menu_options'),
        ('opendata', '0018_alter_opendata_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opendata',
            name='menu',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='opendata', to='menu.menu', verbose_name='Menyu'),
        ),
    ]
