# Generated by Django 4.0.3 on 2022-05-17 04:09

from django.db import migrations, models
import django.db.models.deletion
import internship.models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0013_alter_intern_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nomi')),
                ('photo', models.ImageField(upload_to=internship.models.directory, verbose_name='Foto')),
                ('intern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='internship.intern', verbose_name='Amliyotchi')),
            ],
            options={
                'verbose_name': 'Amaliyotchi',
                'verbose_name_plural': 'Amaliyotchilar',
                'db_table': 'internship_photo',
            },
        ),
    ]