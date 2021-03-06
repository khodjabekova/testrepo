# Generated by Django 4.0.3 on 2022-05-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0015_alter_intern_options_alter_intern_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='name',
            field=models.CharField(max_length=200, verbose_name='To‘liq ismi'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='To‘liq ismi'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='To‘liq ismi'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='name_uz',
            field=models.CharField(max_length=200, null=True, verbose_name='To‘liq ismi'),
        ),
        migrations.AlterField(
            model_name='intern',
            name='name_uzb',
            field=models.CharField(max_length=200, null=True, verbose_name='To‘liq ismi'),
        ),
    ]
