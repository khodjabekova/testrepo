# Generated by Django 4.0.3 on 2022-05-17 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statisticsapp', '0036_alter_annualcost_options_equipmentpurchasestatistics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interncount',
            options={'verbose_name': 'Mamlakatlar', 'verbose_name_plural': 'Mamlakatlar'},
        ),
        migrations.AlterField(
            model_name='interncount',
            name='count',
            field=models.PositiveIntegerField(verbose_name='Mamlakatlar'),
        ),
    ]
