from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit

from baseapp.models import BaseModel
from config.utils import unique_slug_generator

def directory(instance, filename):
    return 'internship/{}/{}'.format(instance.slug, filename)

def photos_directory(instance, filename):
    return 'internship/{}/{}'.format(instance.intern.slug, filename)


class Intern(BaseModel):
    name = models.CharField(max_length=200, verbose_name="To‘liq ismi")
    position = models.CharField(
        max_length=500, null=True, blank=True, verbose_name="Lavozimi")
    place = models.CharField(max_length=500, null=True,
                             blank=True, verbose_name="Amaliyot joyi")
    phone = models.CharField(max_length=14, null=True,
                             blank=True, verbose_name="Telefon")
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True,
                              verbose_name="Elektron pochta manzil")
    biography = models.TextField(
        null=True, blank=True, verbose_name="Amaliyotchi haqida")
    start_date = models.DateField(
        null=True, blank=True, verbose_name="Boshlanish vaqti")
    end_date = models.DateField(
        null=True, blank=True, verbose_name="Tugash vaqti")
    photo = models.ImageField(
        upload_to=directory, null=True, blank=True, verbose_name="Rasm")
    thumbnail = ImageSpecField(source='photo', processors=[ResizeToFit(500)], )
    capture = ImageSpecField(source='photo', processors=[
                             ResizeToFit(30)], options={'quality': 60})

    class Meta:
        db_table = 'internship'
        verbose_name = "Yosh olimlar"
        verbose_name_plural = "Yosh olimlar"

    def __str__(self):
        return self.name


class InternPhoto(models.Model):
    intern = models.ForeignKey(
        Intern, on_delete=models.CASCADE, related_name='photos', verbose_name='Amliyotchi')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nomi")
    photo = models.ImageField(upload_to=photos_directory, verbose_name="Foto")
    capture = ImageSpecField(source='photo', processors=[
                             ResizeToFit(30)], options={'quality': 60})
    class Meta:
        db_table = 'internship_photo'
        verbose_name = "Amaliyotchi"
        verbose_name_plural = "Amaliyotchilar"


def slug_generator(instance, *args, **kwargs):
    if not instance.slug:
        name = ''
        if instance.name_uz is not None and instance.name_uz != '':
            name = instance.name_uz
        if instance.name_ru is not None and instance.name_ru != '':
            name = instance.name_ru
        if instance.name_uzb is not None and instance.name_uzb != '':
            name = instance.name_uzb
        if instance.name_en is not None and instance.name_en != '':
            name = instance.name_en
        else:
            name = get_random_string(8, '0123456789')

        instance.slug = unique_slug_generator(instance, title=name)


pre_save.connect(slug_generator, sender=Intern)
