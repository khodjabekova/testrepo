# Generated by Django 4.0.3 on 2022-04-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_menu_link_alter_menu_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['index'], 'verbose_name': 'Menyu', 'verbose_name_plural': 'Menyular'},
        ),
        migrations.AddField(
            model_name='menu',
            name='index',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tartib raqami'),
        ),
    ]
