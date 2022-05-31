from django.db import models

from baseapp.models import BaseModel


class Faq(BaseModel):
    slug = None
    question = models.CharField(max_length=500, verbose_name="Savol")
    answer = models.TextField(verbose_name="Javob")
    index = models.IntegerField(null=True, blank=True, verbose_name="Tartib raqami")

    class Meta:
        db_table = "faq"
        verbose_name = "Ko'p so'raladigan savol "
        verbose_name_plural = "Ko'p so'raladigan savollar"
        ordering = ['index']

    def __str__(self):
        return self.question
