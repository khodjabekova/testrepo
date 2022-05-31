# Generated by Django 4.0.3 on 2022-04-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0003_intern_biography_en_intern_biography_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern',
            name='biography',
            field=models.TextField(blank=True, null=True, verbose_name='Amaliyotchi haqida: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='biography_en',
            field=models.TextField(blank=True, null=True, verbose_name='Amaliyotchi haqida: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='biography_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Amaliyotchi haqida: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='biography_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Amaliyotchi haqida: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='biography_uzb',
            field=models.TextField(blank=True, null=True, verbose_name='Amaliyotchi haqida: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True, verbose_name='Elektron pochta manzil: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='internship',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Amaliyot joyi va muddati: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='internship_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Amaliyot joyi va muddati: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='internship_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Amaliyot joyi va muddati: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='internship_uz',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Amaliyot joyi va muddati: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='internship_uzb',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Amaliyot joyi va muddati: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='name',
            field=models.CharField(max_length=200, verbose_name="To'liq ism: "),
        ),
        migrations.AlterField(
            model_name='intern',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name="To'liq ism: "),
        ),
        migrations.AlterField(
            model_name='intern',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name="To'liq ism: "),
        ),
        migrations.AlterField(
            model_name='intern',
            name='name_uz',
            field=models.CharField(max_length=200, null=True, verbose_name="To'liq ism: "),
        ),
        migrations.AlterField(
            model_name='intern',
            name='name_uzb',
            field=models.CharField(max_length=200, null=True, verbose_name="To'liq ism: "),
        ),
        migrations.AlterField(
            model_name='intern',
            name='phone',
            field=models.PositiveBigIntegerField(blank=True, max_length=12, null=True, verbose_name='Telefon raqam: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='position',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Lavozimi: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='position_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Lavozimi: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='position_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Lavozimi: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='position_uz',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Lavozimi: '),
        ),
        migrations.AlterField(
            model_name='intern',
            name='position_uzb',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Lavozimi: '),
        ),
    ]