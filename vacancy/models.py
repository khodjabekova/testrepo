from django.db import models


from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string

from baseapp.models import BaseModel
from config.utils import unique_slug_generator


class Vacancy(BaseModel):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    content = models.TextField()
    link = models.URLField(null=True, blank=True, verbose_name="Havola")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "vacancy"
        verbose_name = "Vakansiya"
        verbose_name_plural = "Vakansiyalar"


def slug_generator(instance, *args, **kwargs):
    if not instance.slug:
        title = ""
        if instance.title_uz is not None and instance.title_uz != '':
            title = instance.title_uz
        elif instance.title_ru is not None and instance.title_ru != '':
            title = instance.title_ru
        elif instance.title_uzb is not None and instance.title_uzb != '':
            title = instance.title_uzb
        elif instance.title_en is not None and instance.title_en != '':
            title = instance.title_en
        else:
            title = get_random_string(8, '0123456789')
        instance.slug = unique_slug_generator(instance, title=title)


pre_save.connect(slug_generator, sender=Vacancy)
