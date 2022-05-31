from django.contrib import admin

from useful_link.models import UsefulLink
from django_summernote.admin import SummernoteModelAdmin


class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = ["title_uz", 'title_uzb', 'title_ru', 'title_en', 'url']

    exclude = (
        'title',
        'slug',
        'created_by',
        'updated_by'
    )

    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "Tanlanganlarni o'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(UsefulLink, UsefulLinkAdmin)
