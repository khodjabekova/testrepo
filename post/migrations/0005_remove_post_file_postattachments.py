# Generated by Django 4.0.3 on 2022-05-07 04:20

from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
        migrations.CreateModel(
            name='PostAttachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('file', models.FileField(upload_to=post.models.attach_dir, verbose_name='Fayl')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='post.post', verbose_name='Fayllar')),
            ],
        ),
    ]
