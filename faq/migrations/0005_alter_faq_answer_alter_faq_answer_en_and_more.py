# Generated by Django 4.0.3 on 2022-05-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0004_alter_faq_options_faq_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(verbose_name='Javob'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(null=True, verbose_name='Javob'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_ru',
            field=models.TextField(null=True, verbose_name='Javob'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_uz',
            field=models.TextField(null=True, verbose_name='Javob'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_uzb',
            field=models.TextField(null=True, verbose_name='Javob'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='index',
            field=models.IntegerField(blank=True, null=True, verbose_name='Tartib raqami'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=500, verbose_name='Savol'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_en',
            field=models.CharField(max_length=500, null=True, verbose_name='Savol'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='Savol'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_uz',
            field=models.CharField(max_length=500, null=True, verbose_name='Savol'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_uzb',
            field=models.CharField(max_length=500, null=True, verbose_name='Savol'),
        ),
    ]