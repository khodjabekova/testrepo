from django.db import models
from enum import Enum
from config.regions import RegionsEnum


class Contact(models.Model):
    NEW = 0
    ACCEPTED = 1
    REJECTED = 2
    STATUS_CHOICE = (
        (NEW, 'Yangi'),
        (ACCEPTED, 'Qabul qilingan'),
        (REJECTED, 'Rad etilgan'),
    )

    fullname = models.CharField(max_length=200, verbose_name='F.I.SH.')
    phone = models.CharField(max_length=13, verbose_name='Telefon raqami')

    region = models.CharField(
        choices=[(region.name, region.value[0]) for region in RegionsEnum],
        verbose_name="Hududi", max_length=100)
    address = models.CharField(max_length=200, verbose_name='Manzil')
    file = models.FileField(upload_to='ContactFiles', blank=True, null=True,
                            verbose_name='Faylni yuklang')
    mail = models.EmailField(verbose_name='Elektron pochta')
    message = models.TextField(verbose_name='Xabar', max_length=1200)
    reply = models.TextField(blank=True, null=True, verbose_name='Admin javobi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratildi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirildi")
    status = models.IntegerField(choices=STATUS_CHOICE, default=0, verbose_name='Status')

    class Meta:
        db_table = 'appeal'
        verbose_name = 'Murojaat'
        verbose_name_plural = 'Murojaatlar'

    def __str__(self):
        return self.fullname