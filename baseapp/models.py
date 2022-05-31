from django.db import models
import uuid
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True, verbose_name='Aktiv')

    class Meta:
        abstract = True
