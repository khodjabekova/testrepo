from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from config.regions import RegionsEnum
from config.utils import unique_slug_generator
from config.utils import compressImage
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from baseapp.models import BaseModel
from enum import Enum


class Type(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nomi')

    class Meta:
        db_table = 'equipment_type'
        verbose_name = 'Uskuna turi'
        verbose_name_plural = 'Uskuna turlari'

    def __str__(self):
        return self.name


class Equipment(BaseModel):
    name = models.CharField(max_length=500, verbose_name="Nomlanishi")
    content = models.TextField(verbose_name='Tavsifi')
    region = models.CharField(
        choices=[(region.name, region.value[0]) for region in RegionsEnum],
        verbose_name="Hududlar", max_length=100)
    cover = models.ImageField(
        upload_to='images', verbose_name="Rasm")
    thumbnail = ImageSpecField(source='cover',
                               processors=[ResizeToFit(370)],
                               options={'quality': 100})
    capture = ImageSpecField(source='cover',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})
    views = models.IntegerField(default=0, blank=True, null=True,
                                verbose_name="Ko'rishlar soni")
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, verbose_name='Turi')
    pub_date = models.DateField(verbose_name="Sanasi")
    on_slider = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Equipment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete()
        if self.images:
            for image in self.images.all():
                print(image)
                image.delete()
        super(Equipment, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "equipment"
        verbose_name = 'Uskuna'
        verbose_name_plural = 'Uskunalar'


class EquipmentImages(models.Model):
    equipment = models.ForeignKey(
        Equipment, related_name='images', on_delete=models.CASCADE, verbose_name="Rasmlar")
    image = models.ImageField(upload_to='EquipmentImages',
                              blank=True, null=True, verbose_name='Foto')
    capture = ImageSpecField(source='image',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})

    class Meta:
        db_table = "equipment_image"
        verbose_name = 'Uskuna rasmi'
        verbose_name_plural = 'Uskuna rasmlari'

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image)
        super(EquipmentImages, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super(EquipmentImages, self).delete(*args, **kwargs)


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        name = ''
        if instance.name_uz is not None and instance.name_uz != '':
            name = instance.name_uz
        elif instance.name_uzb is not None and instance.name_uzb != '':
            name = instance.name_uzb
        elif instance.name_ru is not None and instance.name_ru != '':
            name = instance.name_ru
        elif instance.name_en is not None and instance.name_en != '':
            name = instance.name_en
        else:
            name = get_random_string(8, '0123456789')

        instance.slug = unique_slug_generator(instance, title=name)


pre_save.connect(slug_generator, sender=Equipment)
pre_save.connect(slug_generator, sender=Type)
