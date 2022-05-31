from django import forms
from django.contrib import admin
from tinymce.widgets import TinyMCE

from .models import Faq
from django_summernote.admin import SummernoteModelAdmin


class FaqForm(forms.ModelForm):
    answer_uz = forms.CharField(label="Javob [uz]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    answer_ru = forms.CharField(label="Javob [uzb]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    answer_uzb = forms.CharField(label="Javob [ru]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    answer_en = forms.CharField(label="Javob [en]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)

    class Meta:
        model = Faq
        exclude = (
            'answer',
            'updated_by',
            'updated_by',
        )


class FaqAdmin(admin.ModelAdmin):
    fields = ['is_active', 'index', 'question_uz', 'question_ru', 'question_uzb', 'question_en', 'answer_uz',
              'answer_ru', 'answer_uzb',
              'answer_en']
    list_display = ['question_uz', 'answer_uz']
    # exclude = ['created_by', 'updated_by']
    # summernote_fields = ('answer_uz', 'answer_ru', 'answer_uzb', 'answer_en')

    form = FaqForm

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()
        return super(FaqAdmin, self).save_model(request, obj, form, change)


admin.site.register(Faq, FaqAdmin)
