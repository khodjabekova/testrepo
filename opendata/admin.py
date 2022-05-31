from django import forms
from django.contrib import admin
from opendata.models import Opendata, OpendataAttachments


class OpendataAttachmentsAdmin(admin.TabularInline):
    model = OpendataAttachments
    extra = 1
    exclude = ['name', 'file']
    verbose_name = 'Fayl'
    verbose_name_plural = "Fayllar"


class OpenDataForm(forms.ModelForm):
    class Meta:
        model = Opendata
        exclude = (
        'ilova',
        'title',
        'slug',
        'created_by',
        "updated_by",
        )
        widgets={
            'menu': forms.Select(attrs={'class': 'bootstrap-select', 'data-width':"80%"})
            }
class OpendataAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'ilova', 'menu','link', 'index')
    list_filter = ('menu',  )
    search_fields = ('title_ru', 'title_uz', 'title_uzb', 'title_en','ilova', 'link')
    form = OpenDataForm
    exclude = (
        'ilova',
        'title',
        'slug',
        'created_by',
        "updated_by",
    )

    accounts = ['delete_selected']
    inlines = [OpendataAttachmentsAdmin]

    def delete_selected(self, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "O'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


admin.site.register(Opendata, OpendataAdmin)
