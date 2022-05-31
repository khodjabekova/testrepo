# Generated by Django 4.0.3 on 2022-05-12 05:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import statisticsapp.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statisticsapp', '0034_merge_20220511_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppealStatistics',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('individual', models.IntegerField(blank=True, null=True, verbose_name='Jismoniy shaxs')),
                ('legal', models.IntegerField(blank=True, null=True, verbose_name='Yuridik shaxs')),
                ('closed', models.IntegerField(blank=True, null=True, verbose_name='Yakunlangan')),
                ('repeated', models.IntegerField(blank=True, null=True, verbose_name='Qayta ishlashda')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Murojaatlar statistikasi',
                'verbose_name_plural': 'Murojaatlar statistikasi',
                'db_table': 'appeal_stat',
            },
        ),
        migrations.CreateModel(
            name='AppealQuarterStatistics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('year', models.PositiveIntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032)], default=statisticsapp.models.current_year, verbose_name='Yil')),
                ('quarter', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)], verbose_name='Chorak')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Murojaatlar statistikasi (chorak)',
                'verbose_name_plural': 'Murojaatlar statistikasi (chorak)',
                'db_table': 'appeal_stat_qrt',
                'ordering': ['year', 'quarter'],
            },
        ),
        migrations.CreateModel(
            name='AppealQuarterDetailStatistics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('appeal_type', models.CharField(choices=[('internship', 'Stajirovka bo‘limi orqali'), ('phone', 'Ishonch telefoni orqali'), ('written', 'Yozma ravishda'), ('internet', 'Veb-sayt orqali')], max_length=20, verbose_name='Murojaat turi')),
                ('closed', models.IntegerField(verbose_name='Ko‘rib chiqildi')),
                ('redirected', models.IntegerField(verbose_name='Boshqa tashkilotlarga yuborildi')),
                ('in_progress', models.IntegerField(verbose_name='Ko‘rib chiqilmoqda')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('quarter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='statisticsapp.appealquarterstatistics')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'appeal_stat_qrt_detail',
            },
        ),
    ]