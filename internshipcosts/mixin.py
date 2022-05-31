
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext as _

class PermissionsMixin(models.Model):
    """
    A mixin class that adds the fields and methods necessary to support
    Django's Group and Permission model using the ModelBackend.
    """
    is_superuser = models.BooleanField(_('superuser status'), default=False,
        help_text=_('Designates that this user has all permissions without '
                    'explicitly assigning them.'))
    groups = models.ManyToManyField(Group, verbose_name=_('groups'),
        blank=True, help_text=_('The groups this user belongs to. A user will '
                                'get all permissions granted to each of '
                                'his/her group.'))
    user_permissions = models.ManyToManyField(Permission,
        verbose_name=_('user permissions'), blank=True,
        help_text='Specific permissions for this user.')

    class Meta:
        abstract = True


class WithManagedGroupMixin(object):
    groups = models.ManyToManyField(Group, verbose_name=_('groups'),
        related_name="%(app_label)s_%(class)s",
        blank=True, help_text=_('The groups this user belongs to. A user will '
                            'get all permissions granted to each of '
                            'his/her group.'))