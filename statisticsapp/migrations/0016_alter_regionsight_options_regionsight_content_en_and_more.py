# Generated by Django 4.0.3 on 2022-04-22 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statisticsapp', '0015_alter_financeentity_year_alter_interncount_year_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regionsight',
            options={'verbose_name': 'Mintaqaning diqqatga sazovor joyini ', 'verbose_name_plural': 'Mintaqaning diqqatga sazovor joylari'},
        ),
        migrations.AddField(
            model_name='regionsight',
            name='content_en',
            field=models.TextField(null=True, verbose_name='Kontent'),
        ),
        migrations.AddField(
            model_name='regionsight',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='Kontent'),
        ),
        migrations.AddField(
            model_name='regionsight',
            name='content_uz',
            field=models.TextField(null=True, verbose_name='Kontent'),
        ),
        migrations.AddField(
            model_name='regionsight',
            name='content_uzb',
            field=models.TextField(null=True, verbose_name='Kontent'),
        ),
        migrations.AddField(
            model_name='regionsight',
            name='title_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='regionsight',
            name='title_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='regionsight',
            name='title_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='regionsight',
            name='title_uzb',
            field=models.CharField(max_length=500, null=True, verbose_name='Sarlavha'),
        ),
    ]
