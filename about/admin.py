
from django.contrib import admin
from .models import About, AboutImages
from solo.admin import SingletonModelAdmin
from django import forms
from tinymce.widgets import TinyMCE


class AboutImagesAdmin(admin.TabularInline):
    model = AboutImages
    extra = 1
    verbose_name = 'Rasm'
    verbose_name_plural = 'Rasmlar'


class AboutForm(forms.ModelForm):
    description_uz = forms.CharField(label='Biz haqimizda [uz]',
                                     widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    description_uzb = forms.CharField(label='Biz haqimizda [uzb]', widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), required=False)
    description_ru = forms.CharField(label='Biz haqimizda [ru]', widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), required=False)
    description_en = forms.CharField(label='Biz haqimizda [en]', widget=TinyMCE(
        attrs={'cols': 80, 'rows': 30}), required=False)

    class Meta:
        model = About

        exclude = (
            'description',
            'address',
            'created_by',
            'updated_by',
            'slug',
        )


class AboutAdmin(SingletonModelAdmin):

    form = AboutForm
    exclude = (
        'description',
        'address',
        'created_by',
        'updated_by',
        'slug',
    )
    fieldsets = (
        ("Umumiy ma'lumot", {
            'fields': ('description_uz', 'description_uzb', 'description_ru', 'description_en',)
        }),
        ("Bog'lanish", {
            'fields': ('email', "phone", 'address_uz', 'address_uzb', 'address_ru', 'address_en', 'transport_uz', 'transport_uzb', 'transport_ru', 'transport_en', 'youtube_url', 'facebook_url', 'instagram_url', 'telegram_url', 'lng', 'ltd')
        }),
    )
    inlines = [AboutImagesAdmin]


admin.site.register(About, AboutAdmin)
