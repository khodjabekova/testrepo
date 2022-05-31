from baseapp.models import BaseModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from config.utils import unique_slug_generator
from mptt.models import MPTTModel, TreeForeignKey
from enum import Enum


class TypeList(Enum):
    singlepage = ["Bitta sahifa", "Битта сахифа",
                  "Одна страница", "Single page"]
    post = ["Post", "Пост", "Пост", "Post"]
    attachment = ["Ilovali ro'yxat", "Список с вложениями", "Иловали руйхат", "List with attachments"]
    menu = ["Menyu", "Меню", "Меню", "Menu"]
    photogallery = ["Foto galereya", "Меню", "Меню", "Menu"]
    videogallery = ["Video galereya", "Меню", "Меню", "Menu"]
    equipments = ["Asbob uskunalar", "Меню", "Меню", "Menu"]
    internship = ["Stajirovka", "Меню", "Меню", "Menu"]
    other = ["Boshqa", "Бошка", "Другое", "Other"]


class Menu(BaseModel, MPTTModel):
    title = models.CharField(max_length=500, verbose_name="Nomlanishi")
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, related_name='sub_menu',
                            null=True, blank=True, verbose_name="YuqoriMenyu")
    type = models.CharField(
        choices=[(tag.name, tag.value[0]) for tag in TypeList], verbose_name="Turi", max_length=100,
        default=TypeList.other)
    link = models.CharField(max_length=500, null=True,
                            blank=True, verbose_name="Havola")
    index = models.IntegerField(
        null=True, blank=True, verbose_name="Tartib raqami")
    note = models.TextField(max_length=2500, null=True, blank=True, verbose_name="Izoh")

    class Meta:
        ordering = ['index']
        db_table = "menu"
        verbose_name = 'Menyu'
        verbose_name_plural = 'Menyu'

    @property
    def active_sub_menu(self):
        return self.sub_menu.filter(is_active=True)

    class MPTTMeta:
        order_insertion_by = ['index']

    def __str__(self):
        return self.title


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


pre_save.connect(slug_generator, sender=Menu)
