from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.utils.crypto import get_random_string
from django.db.models.signals import pre_save

from config.utils import unique_slug_generator
from baseapp.models import BaseModel


class EventType(models.Model):
    name = models.CharField(max_length=300, verbose_name='Nomi')
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'event_type'
        verbose_name = 'Tadbir turi'
        verbose_name_plural = 'Tadbir turlari'

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


pre_save.connect(slug_generator, sender=EventType)


class Event(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Mavzu')
    main_topic = models.TextField(verbose_name='Asosiy mazmuni')
    content = models.TextField(verbose_name='Matn')
    start_time = models.DateTimeField(verbose_name='Boshlanish vaqti')
    end_time = models.DateTimeField(verbose_name='Tugash vaqti')
    responsible_org = models.CharField(max_length=255, verbose_name="Mas'ul tashkilot")
    address = models.CharField(max_length=255, verbose_name='Manzil')
    type = models.ForeignKey(EventType, on_delete=models.SET_NULL, blank=True, null=True,
                             verbose_name='Tadbir tur')
    pub_date = models.DateField(verbose_name="E'lon Sanasi", blank=True, null=True)
    views = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")

    class Meta:
        db_table = 'event'
        verbose_name = 'Tadbir'
        verbose_name_plural = 'Tadbirlar'
        ordering = ['-start_time']

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


pre_save.connect(slug_generator, sender=Event)


class EventImages(models.Model):
    event = models.ForeignKey(
        Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='EventImages', blank=True, null=True, verbose_name="Rasm")
    thumbnail = ImageSpecField(source="image", processors=[ResizeToFit(700)],
                               options={'quality': 100})

    class Meta:
        db_table = 'event_images'
        verbose_name = 'Tadbir Rasmi'
        verbose_name_plural = 'Tadbir Rasmlari'

    def __str__(self):
        return f"{self.event.title}'s images"
