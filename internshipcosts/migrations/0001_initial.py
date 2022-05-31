# Generated by Django 4.0.3 on 2022-05-17 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import internshipcosts.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InternUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name='Ism')),
                ('lastname', models.CharField(max_length=100, verbose_name='Familiya')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Otasining ismi')),
                ('phone', models.CharField(max_length=14, verbose_name='Telefon Raqami')),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Erkak'), (2, 'Ayol')], verbose_name='Jinsi')),
                ('citizenship', models.CharField(max_length=150, verbose_name='Fuqarolik')),
                ('pnfl', models.CharField(max_length=14, verbose_name='JSH SHIR')),
                ('passport_no', models.CharField(max_length=9, verbose_name='Pasport seriyasi va raqami')),
                ('date_of_birth', models.DateField(verbose_name='Tug‘ilgan sanasi')),
                ('region', models.CharField(choices=[('andijon', 'Andijon viloyati'), ('buxoro', 'Buxoro viloyati'), ('jizzax', 'Jizzax viloyati'), ('qashqadaryo', 'Qashqadaryo viloyati'), ('navoiy', 'Navoiy viloyati'), ('namangan', 'Namangan viloyati'), ('samarqand', 'Samarqand viloyati'), ('surxondaryo', 'Surxondaryo viloyati'), ('sirdaryo', 'Sirdaryo viloyati'), ('toshkent', 'Toshkent viloyati'), ('fargona', 'Fargʻona viloyati'), ('xorazm', 'Xorazm viloyati'), ('qoraqalpogiston', 'Qoraqalpogʻiston Respublikasi'), ('toshkentsh', 'Toshkent shahar')], max_length=100, verbose_name='Hudud')),
                ('address', models.CharField(max_length=255, verbose_name='Yashash manzili')),
                ('photo', models.ImageField(upload_to=internshipcosts.models.intern_user_directory, verbose_name='Foto')),
                ('work_region', models.CharField(choices=[('andijon', 'Andijon viloyati'), ('buxoro', 'Buxoro viloyati'), ('jizzax', 'Jizzax viloyati'), ('qashqadaryo', 'Qashqadaryo viloyati'), ('navoiy', 'Navoiy viloyati'), ('namangan', 'Namangan viloyati'), ('samarqand', 'Samarqand viloyati'), ('surxondaryo', 'Surxondaryo viloyati'), ('sirdaryo', 'Sirdaryo viloyati'), ('toshkent', 'Toshkent viloyati'), ('fargona', 'Fargʻona viloyati'), ('xorazm', 'Xorazm viloyati'), ('qoraqalpogiston', 'Qoraqalpogʻiston Respublikasi'), ('toshkentsh', 'Toshkent shahar')], max_length=100, verbose_name='Ish hududi')),
                ('work', models.CharField(max_length=255, verbose_name='Muassasa')),
                ('work_address', models.CharField(max_length=255, verbose_name='Ish joyining manzili')),
                ('education', models.PositiveSmallIntegerField(choices=[(1, "Oliy ta'lim"), (2, "Oliy ta'limdan keyingi ta'lim")], verbose_name="Ta'lim")),
                ('specialization', models.CharField(max_length=255, verbose_name='Diplom bo‘yicha mutaxassisligi')),
                ('diplom', models.FileField(upload_to=internshipcosts.models.intern_user_directory, verbose_name='Mutaxassisligini tasdiqlovchi hujjat')),
                ('phd_diplom', models.FileField(blank=True, null=True, upload_to=internshipcosts.models.intern_user_directory, verbose_name='Phd diplom nusxasi')),
                ('ielts', models.FileField(blank=True, null=True, upload_to='', verbose_name='Ielts sertifikat nusxasi')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Yangi'), (2, 'Qabul qilindi'), (3, 'Rad etildi')], default=1, verbose_name='Status')),
                ('reason', models.TextField(blank=True, null=True, verbose_name='Rad etish sababi')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Stajor',
                'verbose_name_plural': 'Stajorlar',
                'db_table': 'intern_user',
            },
        ),
        migrations.CreateModel(
            name='InternshipExpenses',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('intern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internshipcosts.internuser')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Stajirovka xarajatlari',
                'verbose_name_plural': 'Stajirovka xarajatlari',
                'db_table': 'internship_expenses',
            },
        ),
        migrations.CreateModel(
            name='FinancialReport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('file', models.FileField(upload_to=internshipcosts.models.internship_expenses_directory, verbose_name='Hisobot')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('internship_expenses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='financial_report', to='internshipcosts.internshipexpenses')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Moliyaviy hisobot',
                'verbose_name_plural': 'Moliyaviy hisobot',
                'db_table': 'internship_financial_report',
            },
        ),
        migrations.CreateModel(
            name='CostStatement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('type', models.CharField(choices=[('daily', 'Sutkalik xarajatlar'), ('accommodation', 'Yashash(turar joy) xarajatlar'), ('insurance', "Sug'urta xarajatlari"), ('transport', 'Transport xarajatlari'), ('internship', 'Stajirovka xarajatlari')], max_length=50, verbose_name='Xarajat turi')),
                ('days', models.IntegerField(blank=True, null=True, verbose_name='Kunlar soni')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('cost', models.BigIntegerField()),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('screenshot', models.FileField(blank=True, null=True, upload_to=internshipcosts.models.internship_expenses_directory)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('internship_expenses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost_statements', to='internshipcosts.internshipexpenses')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Xarajatlar asosnomasi',
                'verbose_name_plural': 'Xarajatlar asosnomasi',
                'db_table': 'internship_cost_statement',
            },
        ),
    ]