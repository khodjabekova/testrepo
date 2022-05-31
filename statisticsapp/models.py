import datetime

from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit

from baseapp.models import BaseModel
from .country import CountryEnum
# Create your models here.
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from config.utils import unique_slug_generator
from config.regions import RegionsEnum
from .types import FinanceEntityType
from solo.models import SingletonModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year + 11)]


def current_year():
    return datetime.date.today().year


class Country(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Mamlakat")
    code = models.CharField(unique=True,
                            choices=[(c.name, f"{c.value[0]} - {c.name}")
                                     for c in CountryEnum],
                            verbose_name="Mamlakatlar kodi", max_length=100)

    class Meta:
        db_table = "country"
        verbose_name = "Xorijiy davlatlar"
        verbose_name_plural = "Xorijiy davlatlar"

    def __str__(self):
        return self.name


class ScienceField(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Yo‘nalish nomi")
    icon = models.FileField(verbose_name="Logotip")
    index = models.IntegerField(null=True, blank=True, verbose_name="Tartib raqami")
    class Meta:
        ordering = ['index']
        db_table = "science_field"
        verbose_name = "Yo‘nalish"
        verbose_name_plural = "Yo‘nalishlar"

    def __str__(self):
        return self.name


class ScientificInternship(BaseModel):
    slug = None
    year = models.PositiveIntegerField(
        verbose_name="Yil", choices=year_choices(), default=current_year)
    region = models.CharField(choices=[(region.name, region.value[0]) for region in RegionsEnum],
                              verbose_name="Hudud", max_length=200)
    successful = models.PositiveIntegerField(verbose_name="Muvaffaqiyatli")
    rejected = models.PositiveIntegerField(verbose_name="Rad etilgan")

    class Meta:
        db_table = "scientific_internship"
        verbose_name = "Startap loyihalarni moliyalashtirish"
        verbose_name_plural = "Startap loyihalarni moliyalashtirish"
        unique_together = ['year', 'region']

    def __str__(self):
        return self.region


class ScientificInternshipStatistic(BaseModel):
    slug = None
    field = models.ForeignKey(ScienceField, on_delete=models.CASCADE, related_name='statistics',
                              verbose_name="Yo'nalish")
    amount = models.PositiveBigIntegerField(verbose_name="Mablag‘")
    scientific_internship = models.ForeignKey(ScientificInternship, related_name='statistics', on_delete=models.CASCADE,
                                              verbose_name="Ilmiy stajirovka")

    class Meta:
        db_table = "scientific_internship_statistic"
        verbose_name = "Startap loyihalarni moliyalashtirish yo‘nalishlar kesmida"
        verbose_name_plural = "Startap loyihalarni moliyalashtirish yo‘nalishlar kesmida"


class CountryStatistics(BaseModel):
    slug = None
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='statistics', verbose_name="Mamlakat")
    science_field = models.ForeignKey(
        ScienceField, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Yo‘nalish")
    count = models.BigIntegerField(verbose_name="Soni")

    class Meta:
        db_table = "country_statistics"
        verbose_name = "Mamlakat statistikasi"
        verbose_name_plural = "Mamlakat statistikalari"

    def __str__(self):
        return f"{self.country.name} {self.science_field}"


class FinanceEntity(BaseModel):
    slug = None
    type = models.CharField(max_length=1000,
                            choices=[(finance.name, finance.value[0])
                                     for finance in FinanceEntityType],
                            verbose_name="Turi")
    year = models.IntegerField(
        choices=year_choices(), default=current_year, verbose_name="Yil")
    sum = models.PositiveBigIntegerField()

    class Meta:
        db_table = "finance_entity"
        verbose_name = "Innovatsion faoliyat subyektlarini moliyalashtirish"
        verbose_name_plural = "Innovatsion faoliyat subyektlarini moliyalashtirish"
        unique_together = ['type', 'year']

    def __str__(self):
        return self.type


class Region(BaseModel):
    slug = None
    name = models.CharField(unique=True,
                            choices=[(region.name, region.value[0])
                                     for region in RegionsEnum],
                            verbose_name="Hudud", max_length=100)

    class Meta:
        db_table = "region"
        verbose_name = "Hudud"
        verbose_name_plural = "Hududlar"

    def __str__(self):
        return self.name


class RegionStatistics(BaseModel):
    slug = None
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='statistics', verbose_name="Hudud")
    science_field = models.ForeignKey(
        ScienceField, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Yo‘nalish")
    count = models.BigIntegerField(verbose_name="Soni")

    class Meta:
        db_table = "region_statistics"
        verbose_name = "Hudud statistikasi"
        verbose_name_plural = "Hudud statistikalari"
        unique_together = ['region', 'science_field']

    def __str__(self):
        return f"{self.region.name} {self.science_field}"


class RegionSight(BaseModel):
    title = models.CharField(max_length=500, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Kontent")
    region = models.CharField(
        choices=[(region.name, region.value[0]) for region in RegionsEnum], max_length=1000)
    image = models.ImageField(
        upload_to="images/region-sights", verbose_name="Rasm")
    thumbnail = ImageSpecField(source='image', processors=[
                               ResizeToFit(370)], options={'quality': 100})
    capture = ImageSpecField(source='image', processors=[
                             ResizeToFit(30)], options={'quality': 60})

    class Meta:
        db_table = "region_sight"
        verbose_name = "Mintaqaning diqqatga sazovor joyi"
        verbose_name_plural = 'Mintaqaning diqqatga sazovor joylari'

    def __str__(self):
        return self.title


class RegionSightImages(models.Model):
    title = models.ForeignKey(RegionSight, related_name="images",
                              on_delete=models.CASCADE, verbose_name="Sarlavha")
    image = models.ImageField(
        upload_to='images/region-sights/images', verbose_name="Rasm")
    thumbnail = ImageSpecField(source='image', processors=[
                               ResizeToFit(370)], options={'quality': 100})
    capture = ImageSpecField(source='image', processors=[
                             ResizeToFit(30)], options={'quality': 60})

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'region_sight_images'
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        return super(RegionSightImages, self).delete(*args, **kwargs)


class YoungScientistInternship(BaseModel):
    """
    Yosh olimlarni ilmiy stajirovkaga yuborish bo'yicha statistik ma'lumot
    """
    slug = None
    scientist = models.PositiveIntegerField(verbose_name="Yosh olimlar soni")
    country = models.PositiveIntegerField(verbose_name="Davlatlar soni")
    field = models.PositiveIntegerField(verbose_name="Yo'nalishlar soni")
    relation = models.PositiveIntegerField(verbose_name="Aloqalar soni")

    class Meta:
        db_table = "young_scientist_internship"
        verbose_name = "Bosh sahifadagi statistika"
        verbose_name_plural = "Bosh sahifadagi statistika"

    def __str__(self):
        return f"{self.scientist}"





class InternCount(BaseModel):
    slug = None
    year = models.IntegerField(choices=year_choices(
    ), unique=True, default=current_year, verbose_name="Yil")
    count = models.PositiveIntegerField(verbose_name="Mamlakatlar")

    class Meta:
        db_table = "intern_count"
        verbose_name = "Yosh olimlar yillar kesmida"
        verbose_name_plural = "Yosh olimlar yillar kesmida"

    def __str__(self):
        return f"{self.year}"


class AnnualCost(BaseModel):
    slug = None
    year = models.IntegerField(unique=True, choices=year_choices(
    ), default=current_year, verbose_name="Yil: ")
    fields = models.PositiveIntegerField(verbose_name="Turlar soni: ")
    cost = models.PositiveBigIntegerField(verbose_name="Yillik xarajat: ")

    class Meta:
        db_table = "annual_cost"
        verbose_name = "Asbob-uskunalar"
        verbose_name_plural = "Asbob-uskunalar (turlar bo'yicha)"
        ordering = ['year']

    def __str__(self):
        return f"{self.year}"


class NormativeDocument(BaseModel):
    slug = None
    date = models.DateField(verbose_name="Sana")
    count = models.PositiveIntegerField()

    class Meta:
        db_table = "normative_documents"
        verbose_name = "Me'yoriy hujjat"
        verbose_name_plural = "Me'yoriy hujjatlar"

    def __str__(self):
        return f"{self.date} - {self.count}"


class AppealStatistics(SingletonModel, BaseModel):
    slug = None
    id = models.AutoField(primary_key=True)
    individual = models.IntegerField(
        null=True, blank=True, verbose_name="Jismoniy shaxs")
    legal = models.IntegerField(
        null=True, blank=True, verbose_name="Yuridik shaxs")
    closed = models.IntegerField(
        null=True, blank=True, verbose_name="Yakunlangan")
    repeated = models.IntegerField(
        null=True, blank=True, verbose_name="Qayta ishlashda")

    class Meta:
        db_table = "appeal_stat"
        verbose_name = "Murojaatlar statistikasi"
        verbose_name_plural = "Murojaatlar statistikasi"


class AppealQuarterStatistics(BaseModel):
    slug = None
    year = models.PositiveIntegerField(
        verbose_name="Yil", choices=year_choices(), default=current_year)
    quarter = models.IntegerField(validators=[MaxValueValidator(
        4), MinValueValidator(1)], verbose_name="Chorak")

    class Meta:
        db_table = "appeal_stat_qrt"
        verbose_name = "Murojaatlar statistikasi (chorak)"
        verbose_name_plural = "Murojaatlar statistikasi (chorak)"
        ordering = ['year', 'quarter']

    def __str__(self) -> str:
        return f"{self.year} yil {self.quarter} chorak"


class AppealQuarterDetailStatistics(BaseModel):
    APPEAL_CHOICE = (
        ('internship', 'Stajirovka bo‘limi orqali'),
        ('phone', 'Ishonch telefoni orqali'),
        ('written', 'Yozma ravishda'),
        ('internet', 'Veb-sayt orqali'),
    )
    slug = None
    quarter = models.ForeignKey(
        AppealQuarterStatistics, related_name="statistics", on_delete=models.CASCADE)
    appeal_type = models.CharField(max_length=20,
                                   choices=APPEAL_CHOICE, verbose_name="Murojaat turi")
    closed = models.IntegerField(verbose_name="Ko‘rib chiqildi")
    redirected = models.IntegerField(
        verbose_name="Boshqa tashkilotlarga yuborildi")
    in_progress = models.IntegerField(verbose_name="Ko‘rib chiqilmoqda")

    class Meta:
        db_table = "appeal_stat_qrt_detail"


class EquipmentPurchaseStatistics(BaseModel):
    title = models.TextField(max_length=500, verbose_name='Qisqacha tavsif')
    equipment_count = models.PositiveBigIntegerField(
        verbose_name='Turlar soni')
    invested = models.PositiveBigIntegerField(
        verbose_name='So‘m yo‘naltirilgan')
    index = models.IntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        db_table = "equipment_purchased"
        verbose_name = "Laboratoriya uskunalari statistikasi"
        verbose_name_plural = "Laboratoriya uskunalari statistikasi"

    def __str__(self):
        return self.title


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


def slug_generator_title(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, title=instance.title)


pre_save.connect(slug_generator, sender=Country)
pre_save.connect(slug_generator, sender=ScienceField)
pre_save.connect(slug_generator_title, sender=EquipmentPurchaseStatistics)
pre_save.connect(slug_generator_title, RegionSight)


class FinanceInternshipYear(BaseModel):
    slug = None
    year = models.PositiveIntegerField(unique=True,
        verbose_name="Yil", choices=year_choices(), default=current_year)

    class Meta:
        db_table = "finance_internship_year"
        verbose_name = "Ilmiy stajirovkalarni moliyalashtirish"
        verbose_name_plural = "Ilmiy stajirovkalarni moliyalashtirish"

    def __str__(self):
        return str(self.year)

class FinanceInternshipStatistics(BaseModel):
    slug = None
    year = models.ForeignKey(FinanceInternshipYear, related_name='statistics', on_delete=models.CASCADE)
    field = models.ForeignKey(ScienceField, on_delete=models.PROTECT)
    amount = models.PositiveBigIntegerField(verbose_name="Mablag‘")

    class Meta:
        db_table = "finance_internship_stat"
        unique_together = ('year', 'field')
        verbose_name = "Ilmiy stajirovkalarni moliyalashtirish"
        verbose_name_plural = "Ilmiy stajirovkalarni moliyalashtirish"

    def __str__(self):
        return str(self.year)