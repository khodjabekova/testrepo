from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from baseapp.models import BaseModel
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from config.utils import unique_slug_generator
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.conf import settings
import shutil
import os
from bs4 import BeautifulSoup

class Department(BaseModel, MPTTModel):

    name = models.CharField(max_length=500, verbose_name="Boʻlim nomi")
    index = models.IntegerField(
        null=True, blank=True, verbose_name="Tartib raqami")
    parent = TreeForeignKey('self', on_delete=models.SET_NULL,
                            null=True, blank=True, related_name='sub_departments', verbose_name="Yuqori boʻlim")

    class Meta:
        db_table = "department"
        verbose_name = "Boʻlim"
        verbose_name_plural = "Boʻlimlar"

    class MPTTMeta:
        order_insertion_by = ['index']

    def __str__(self):
        return self.name


class Employee(BaseModel):
    name = models.CharField(max_length=250, verbose_name="Toʻliq ismi")
    email = models.CharField(max_length=250, null=True,
                             blank=True, verbose_name="E-mail")
    phone = models.CharField(max_length=250, null=True, blank=True,
                             verbose_name="Telefon raqami")
    internal_number = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="Ichki raqami")
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, related_name='employee_list', null=True, verbose_name="Boʻlim")
    position = models.CharField(
        max_length=250, null=True, verbose_name="Lavozimi")
    working_hours = models.CharField(
        max_length=250, null=True, verbose_name="Qabul vaqtlari")
    leadership = models.BooleanField(
        default=False, null=True, blank=True, verbose_name="Rahbariyat")
    is_chief = models.BooleanField(
        default=False, verbose_name="Boʻlim boshligʻi")
    photo = models.ImageField(upload_to='employee',
                              null=True, blank=True, verbose_name="Rasm")
    thumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFit(370)])
    capture = ImageSpecField(source='photo',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})
    biography = models.TextField(
        null=True, blank=True, verbose_name="Tarjimai holi")
    responsibilities = models.TextField(
        null=True, blank=True, verbose_name="Majburiyatlari")
    index = models.IntegerField(null=True, blank=True, verbose_name="Tartib raqami")

    class Meta:
        db_table = "employee"
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        ordering = ['index']

    def __str__(self):
        return self.name
   
    def delete(self, *args, **kwargs):

        if self.photo:
            self.photo.delete()
        
        content = self.biography_uz +self.biography_uzb +self.biography_ru +self.biography_en +\
                        self.responsibilities_uz +self.responsibilities_uzb +self.responsibilities_ru +self.responsibilities_en
        tags = BeautifulSoup(content).findAll('img')
       
        for image in tags:
            file = image['src'].split('/')[-1]
            path = os.path.join(settings.MEDIA_ROOT, 'tinymce', file)
            try:
                os.remove(path) 
            except: 
                print( "path:", path )
        super(Employee, self).delete(*args, **kwargs)

class SupervisoryBoard(BaseModel):
    name = models.CharField(max_length=500, verbose_name="Ismi")
    position = models.CharField(max_length=500, verbose_name="Lavozimi")
    index = models.IntegerField(
        null=True, blank=True, verbose_name="Tartib raqami")

    class Meta:
        ordering = ['index']
        db_table = "supervisory_board"
        verbose_name = "Kuzatuv kengashi"
        verbose_name_plural = "Kuzatuv kengashi"

    def __str__(self):
        return self.name


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


pre_save.connect(slug_generator, sender=Department)
pre_save.connect(slug_generator, sender=Employee)
pre_save.connect(slug_generator, sender=SupervisoryBoard)
