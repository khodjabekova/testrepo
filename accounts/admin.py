from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserAdminCreationForm, UserAdminChangeForm
User = get_user_model()

from django_summernote.models import Attachment
admin.site.unregister(Attachment)

Group._meta.verbose_name = 'Rol'
Group._meta.verbose_name_plural = 'Rollar'



class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'firstname', 'lastname', ]
    search_fields = ['username', 'firstname', 'lastname', 'email']
    # list_filter = ['role']
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'firstname','lastname',  'groups')}),

    )
    # add_fieldsets = None
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password',)}
        ),
    )

admin.site.register(User, CustomUserAdmin)
