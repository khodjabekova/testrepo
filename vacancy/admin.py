from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from vacancy.models import Vacancy
from django import forms
from tinymce.widgets import TinyMCE


class VacancyForm(forms.ModelForm):
    content_uz = forms.CharField(label='Matn [uz]', widget=TinyMCE(attrs={'cols': 80, "rows": 30}))
    content_uzb = forms.CharField(label='Matn [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_ru = forms.CharField(label='Matn [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_en = forms.CharField(label='Matn [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    list_filter = ('is_active',)

    class Meta:
        model = Vacancy
        exclude = (
            'slug',
            'title',
            'content',
            'created_by',
            'updated_by'
        )


class VacancyAdmin(admin.ModelAdmin):
    # fields = ('title_uz', 'title_ru', 'title_uzb', 'title_en', 'content_uz', 'content_ru', 'content_uzb', 'content_en',)
    list_display = ('title', 'link', 'is_active')
    search_fields = ('title_uz', 'title_ru', 'title_uzb', 'title_en',)

    form = VacancyForm

    # summernote_fields = ('content_uz', 'content_ru', 'content_uzb', 'content_en')

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Vacancy, VacancyAdmin)
