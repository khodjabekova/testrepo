# Generated by Django 4.0.3 on 2022-05-26 14:02

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_postattachments_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=post.models.image_dir, verbose_name='Asosiy rasm'),
        ),
        migrations.AlterField(
            model_name='postimages',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=post.models.attach_dir, verbose_name='Foto'),
        ),
    ]
