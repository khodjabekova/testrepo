
import os
import shutil
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from config.utils import unique_slug_generator, compressImage
from django.utils.crypto import get_random_string
from django.utils.timezone import now

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from bs4 import BeautifulSoup
from mptt.models import TreeForeignKey

from baseapp.models import BaseModel
from menu.models import Menu



# class Tags(BaseModel):
#     name = models.CharField(max_length=255, verbose_name="Teg nomi")

#     class Meta:
#         db_table = "post_tag"
#         verbose_name = 'Teg'
#         verbose_name_plural = 'Teglar'
#         ordering = ['-created_at']

#     def __str__(self):
#         return self.name


# def slug_generator(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         name = ''
#         if instance.name_uz is not None and instance.name_uz != '':
#             name = instance.name_uz
#         elif instance.name_uzb is not None and instance.name_uzb != '':
#             name = instance.name_uzb
#         elif instance.name_ru is not None and instance.name_ru != '':
#             name = instance.name_ru
#         elif instance.name_en is not None and instance.name_en != '':
#             name = instance.name_en
#         else:
#             name = get_random_string(8, '0123456789')

#         instance.slug = unique_slug_generator(instance, title=name)


# pre_save.connect(slug_generator, sender=Tags)

def image_dir(instance, filename):
    return 'post/{}/{}'.format(instance.slug, filename)
    
def attach_dir(instance, filename):
    return 'post/{}/{}'.format(instance.post.slug, filename)



class Post(BaseModel):
    title = models.CharField(max_length=500, verbose_name="Sarlavha")
    content = models.TextField(null=True, blank=True, verbose_name="Matni")
    photo = models.ImageField(upload_to=image_dir,
                              null=True, blank=True, verbose_name="Asosiy rasm")
    thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFit(370)])
    capture = ImageSpecField(source='photo',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})

    menu = TreeForeignKey(Menu, null=True, blank=True, related_name='posts',
                             on_delete=models.SET_NULL, verbose_name='Menyu')

    views = models.IntegerField(default=0, blank=True, null=True,
                                verbose_name="Ko'rishlar Soni")
    pub_date = models.DateField(default=now, verbose_name="Sanasi")
    on_slider = models.BooleanField(default=False)
    # file = models.FileField(upload_to=directory, null=True, blank=True, verbose_name="Fayl")

    class Meta:
        db_table = "post"
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'
        ordering = ['-pub_date', '-created_at']

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):

        if self.photo:
            self.photo.delete()
        for attachment in self.attachments.all():
            attachment.delete()
        for image in self.images.all():
            image.delete()
        folder = os.path.join(settings.MEDIA_ROOT, 'post', self.slug)
        try:
            shutil.rmtree(folder, ignore_errors=True)
        except:
            pass

        content = self.content_uz + self.content_uzb +self.content_ru + self.content_en
        tags = BeautifulSoup(content).findAll('img')
       
        for image in tags:
            file = image['src'].split('/')[-1]
            path = os.path.join(settings.MEDIA_ROOT, 'tinymce', file)
            try:
                os.remove(path) 
            except: 
                print( "path:", path )
        super(Post, self).delete(*args, **kwargs)

class PostAttachments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='attachments', verbose_name='Fayllar')
    name = models.CharField(max_length=255, verbose_name="Nomi")
    file = models.FileField(upload_to=attach_dir, verbose_name="Fayl")

    class Meta:
        db_table = "post_attachments"
        verbose_name = 'Post fayllari'
        verbose_name_plural = 'Postlar fayllari'

    def delete(self, *args, **kwargs):
        if self.file:
            self.file.delete()
        super(PostAttachments, self).delete(*args, **kwargs)

        
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = ''
        if instance.title_uz is not None and instance.title_uz != '':
            title = instance.title_uz
        elif instance.title_uzb is not None and instance.title_uzb != '':
            title = instance.title_uzb
        elif instance.title_ru is not None and instance.title_ru != '':
            title = instance.title_ru
        elif instance.title_en is not None and instance.title_en != '':
            title = instance.title_en
        else:
            title = get_random_string(8, '0123456789')

        instance.slug = unique_slug_generator(instance, title=title)


pre_save.connect(slug_generator, sender=Post)


class PostImages(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE,
                             verbose_name="Rasmlar")
    image = models.ImageField(upload_to=attach_dir,
                              blank=True, null=True, verbose_name=('Foto'))
    capture = ImageSpecField(source='image',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})
    is_active = models.BooleanField(default=True, verbose_name='Aktiv')
    index = models.IntegerField(
        null=True, blank=True, verbose_name="Tartib raqami")

    class Meta:
        db_table = "post_images"
        ordering = ['index']

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image)
        super(PostImages, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super(PostImages, self).delete(*args, **kwargs)
