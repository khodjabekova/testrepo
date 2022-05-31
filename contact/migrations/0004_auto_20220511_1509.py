# Generated by Django 3.2.4 on 2022-05-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Murojaat', 'verbose_name_plural': 'Murojaatlar'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='ContactFiles', verbose_name='Faylni yuklang'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='Elektron pochta'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=13, verbose_name='Telefon raqami'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='reply',
            field=models.TextField(blank=True, null=True, verbose_name='Admin javobi'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.IntegerField(choices=[(0, 'Yangi'), (1, 'Qabul qilingan'), (2, 'Rad etilgan')], default=0, verbose_name='Status'),
        ),
    ]