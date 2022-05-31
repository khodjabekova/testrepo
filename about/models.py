from django.db import models
from solo.models import SingletonModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class About(SingletonModel):
    id = models.IntegerField(primary_key=True, editable=False)
    description = models.TextField(
        blank=True, null=True, verbose_name="Biz haqimizda")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    phone = models.CharField(max_length=50, verbose_name="Telefon")
    facebook_url = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Facebook")
    instagram_url = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Instagram")
    telegram_url = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Telegram")
    youtube_url = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="Youtube")
    address = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="Manzil")
    transport = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="Transport")
    lng = models.DecimalField(
        max_digits=9, decimal_places=6, max_length=200, verbose_name="Uzunlik", null=True, blank=True)
    ltd = models.DecimalField(
        max_digits=9, decimal_places=6, max_length=200, verbose_name="Kenglik ", null=True, blank=True)

    class Meta:
        db_table = 'about'
        verbose_name = "Jamgʻarma haqida"
        verbose_name_plural = "Jamgʻarma haqida"

    def __str__(self) -> str:
        return "Jamgʻarma haqida"


class AboutImages(models.Model):
    about = models.ForeignKey(About, related_name='images', on_delete=models.CASCADE,
                              verbose_name="Rasmlar")
    image = models.ImageField(upload_to='about',
                              blank=True, null=True, verbose_name=('Foto'))
    capture = ImageSpecField(source='image',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})
    is_active = models.BooleanField(default=True, verbose_name='Aktiv')
    index = models.IntegerField(
        null=True, blank=True, verbose_name="Tartib raqami")

    class Meta:
        db_table = "about_images"
        ordering = ['index']
        verbose_name = 'Rasm'
        verbose_name_plural = 'Rasmlar'

    def __str__(self) -> str:
        return "Rasm"
