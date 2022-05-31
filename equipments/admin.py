from django import forms
from django.contrib import admin
from django.db import models
from .models import Equipment, EquipmentImages, Type
from django_summernote.admin import SummernoteModelAdmin
from tinymce.widgets import TinyMCE


class TypeAdmin(admin.ModelAdmin):
    ordering = ('name', )
    fields = ['name_uz', 'name_uzb', 'name_ru', 'name_en', 'is_active']
    list_display = ['name_uz', 'name_uzb', 'name_ru', 'name_en']
    search_fields = ['name_uz', 'name_uzb', 'name_ru', 'name_en']

    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "O'chirish"


class EquipmentImagesAdmin(admin.TabularInline):
    model = EquipmentImages
    extra = 1
    verbose_name = "Tasvir"
    verbose_name_plural = "Tasvirlar"

    formfield_overrides = {
        models.ImageField: {"widget": forms.ClearableFileInput(attrs={'multiple': True})},
    }

class EquipmentForm(forms.ModelForm):
    content_uz = forms.CharField(label="Matn [uz]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    content_uzb = forms.CharField(label="Matn [uzb]",widget=TinyMCE(attrs={'cols': 80, 'rows': 30}),required=False)
    content_ru = forms.CharField(label="Matn [ru]",widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_en = forms.CharField(label="Matn [en]",widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    class Meta:
        model = Equipment
        exclude = ['name', 'created_by', 'updated_by',
               'slug', 'views', 'content']

class EquipmentAdmin(admin.ModelAdmin):
    ordering = ('-created_at', )
    form = EquipmentForm

    exclude = ['name', 'created_by', 'updated_by',
               'slug', 'views', 'content']

    list_display = ['name_uz', 'name_uzb',
                    'name_ru', 'name_en', 'type', 'region']
    search_fields = ['name_uz', 'name_uzb', 'name_ru', 'name_en', 'region']
    fields = ['is_active', 'on_slider', 'region', 'cover', 'type', 'pub_date', 'name_uz', 'name_uzb',
              'name_ru', 'name_en', 'content_uz', 'content_uzb', 'content_ru', 'content_en']
    inlines = [EquipmentImagesAdmin]

    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "O'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user

        obj.save()
        for filename, file in request.FILES.items():
            if filename == 'cover':
                continue
            pictures = request.FILES.getlist(filename)
            for picture in pictures[:-1]:
                EquipmentImages.objects.create(equipment=obj, image=picture)
        return super().save_model(request, obj, form, change)


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Type, TypeAdmin)
