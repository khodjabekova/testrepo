# Generated by Django 4.0.3 on 2022-04-21 12:40

from django.db import migrations, models
import statisticsapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('statisticsapp', '0009_financeentity'),
    ]

    operations = [
        migrations.AddField(
            model_name='financeentity',
            name='type_en',
            field=models.CharField(choices=[('xorijiy_eksportlar', 'Xorijiy ekspertlar (sohalar kesimida)'), ('noyob_qolyozmalar', 'Noyob qo‘lyozmalar'), ('bazadan_foydalanish', 'Yetakchi elektron ilmiy ma’lumotlar bazalaridan erkin foydalanish chop etishga tayyorlash'), ('orolboyi_markazi', 'O‘zbekiston Respublikasi Prezidenti huzuridagi Orolbo‘yi xalqaro innovasiya markazi')], max_length=1000, null=True, verbose_name='Turi'),
        ),
        migrations.AddField(
            model_name='financeentity',
            name='type_ru',
            field=models.CharField(choices=[('xorijiy_eksportlar', 'Xorijiy ekspertlar (sohalar kesimida)'), ('noyob_qolyozmalar', 'Noyob qo‘lyozmalar'), ('bazadan_foydalanish', 'Yetakchi elektron ilmiy ma’lumotlar bazalaridan erkin foydalanish chop etishga tayyorlash'), ('orolboyi_markazi', 'O‘zbekiston Respublikasi Prezidenti huzuridagi Orolbo‘yi xalqaro innovasiya markazi')], max_length=1000, null=True, verbose_name='Turi'),
        ),
        migrations.AddField(
            model_name='financeentity',
            name='type_uz',
            field=models.CharField(choices=[('xorijiy_eksportlar', 'Xorijiy ekspertlar (sohalar kesimida)'), ('noyob_qolyozmalar', 'Noyob qo‘lyozmalar'), ('bazadan_foydalanish', 'Yetakchi elektron ilmiy ma’lumotlar bazalaridan erkin foydalanish chop etishga tayyorlash'), ('orolboyi_markazi', 'O‘zbekiston Respublikasi Prezidenti huzuridagi Orolbo‘yi xalqaro innovasiya markazi')], max_length=1000, null=True, verbose_name='Turi'),
        ),
        migrations.AddField(
            model_name='financeentity',
            name='type_uzb',
            field=models.CharField(choices=[('xorijiy_eksportlar', 'Xorijiy ekspertlar (sohalar kesimida)'), ('noyob_qolyozmalar', 'Noyob qo‘lyozmalar'), ('bazadan_foydalanish', 'Yetakchi elektron ilmiy ma’lumotlar bazalaridan erkin foydalanish chop etishga tayyorlash'), ('orolboyi_markazi', 'O‘zbekiston Respublikasi Prezidenti huzuridagi Orolbo‘yi xalqaro innovasiya markazi')], max_length=1000, null=True, verbose_name='Turi'),
        ),
        migrations.AlterField(
            model_name='financeentity',
            name='year',
            field=models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=statisticsapp.models.current_year, verbose_name='Yil'),
        ),
    ]
