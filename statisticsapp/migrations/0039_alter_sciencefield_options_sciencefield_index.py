# Generated by Django 4.0.3 on 2022-05-23 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statisticsapp', '0038_alter_financeentity_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sciencefield',
            options={'ordering': ['index'], 'verbose_name': 'Yo‘nalish', 'verbose_name_plural': 'Yo‘nalishlar'},
        ),
        migrations.AddField(
            model_name='sciencefield',
            name='index',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tartib raqami'),
        ),
    ]
