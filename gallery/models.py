from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from baseapp.models import BaseModel
from config.utils import unique_slug_generator


class Gallery(BaseModel):
    name = models.CharField(max_length=500, verbose_name="Galereya nomi")
    cover = models.ImageField(upload_to='images/', verbose_name="Asosiy rasm")
    thumbnail = ImageSpecField(source='cover',
                               processors=[ResizeToFit(370)],
                               options={'quality': 100})
    capture = ImageSpecField(source="cover", processors=[
        ResizeToFit(30)], options={'quality': 60})
    on_slider = models.BooleanField(default=False)
    index = models.IntegerField(null=True, blank=True, verbose_name="Tartib raqami")

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

class PhotoGallery(Gallery):
    class Meta:
        db_table = 'photo_gallery'
        verbose_name = "Foto galereya"
        verbose_name_plural = "Foto galereya"
        ordering = ['-index']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(PhotoGallery, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete()
        if self.images:
            for image in self.images.all():
                image.delete()
        super(PhotoGallery, self).delete(*args, **kwargs)


class PhotoGalleryImages(models.Model):
    gallery = models.ForeignKey(
        PhotoGallery, related_name='images', on_delete=models.CASCADE, verbose_name="Tasvirlar")
    image = models.ImageField(
        upload_to='PhotoGallery/', blank=True, null=True, verbose_name="Rasm")
    capture = ImageSpecField(source="image", processors=[
        ResizeToFit(30)], options={'quality': 60})

    class Meta:
        db_table = 'photo_gallery_images'


    # def save(self, *args, **kwargs):
    #     if self.image:
    #         self.image = compressImage(self.image)
    #     super(PhotoGalleryImages, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super(PhotoGalleryImages, self).save(*args, **kwargs)


class VideoGallery(Gallery):
    link = models.CharField(
        max_length=500, verbose_name='Havola', null=True, blank=True)

    class Meta:
        db_table = 'video_gallery'
        verbose_name = "Video galereya"
        verbose_name_plural = 'Video galereya'
        ordering = ['-index']

    def __str__(self):
        return self.name


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        name = ''
        if instance.name_uz is not None and instance.name_uz != "":
            name = instance.name_uz
        elif instance.name_ru is not None and instance.name_ru != "":
            name = instance.name_ru
        elif instance.name_uzb is not None and instance.name_uzb != "":
            name = instance.name_uzb
        elif instance.name_en is not None and instance.name_en != "":
            name = instance.name_en
        else:
            name = get_random_string(8, '0123456789')
        instance.slug = unique_slug_generator(instance, title=name)


pre_save.connect(slug_generator, sender=PhotoGallery)
pre_save.connect(slug_generator, sender=VideoGallery)
