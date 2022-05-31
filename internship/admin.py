from django import forms
from django.contrib import admin
from tinymce.widgets import TinyMCE
from internship.models import Intern, InternPhoto

class InternPhotoAdmin(admin.TabularInline):
    model = InternPhoto
    extra = 1
    exclude = ['name', 'file']
    verbose_name = 'Foto'
    verbose_name_plural = "Foto"

class InternForm(forms.ModelForm):
    biography_uz = forms.CharField(label='Tarjimai hol [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    biography_uzb = forms.CharField(label='Tarjimai hol [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    biography_ru = forms.CharField(label='Tarjimai hol [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    biography_en = forms.CharField(label='Tarjimai hol [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)

    class Meta:
        model = Intern
        exclude = (
            "created_by",
            "updated_by",
            'slug',
            'name',
            'position',
            'internship',
            'biography'
        )


class InternAdmin(admin.ModelAdmin):
    # fields = ['name_uz', 'name_ru', 'name_uzb', 'name_en', 'position_uz', 'position_ru', 'position_uzb', 'position_en',
    #           'place_uz', 'place_ru', 'place_uzb', 'place_en', 'start_date', 'end_date', 'phone', 'email',
    #           'biography_uz',
    #           'biography_ru', 'biography_uzb', 'biography_en', 'photo']
    list_display = ['name', 'position', 'place',
                    'phone', 'email', 'start_date', 'end_date']
    search_fields = ['name_uz', 'name_ru', 'name_uzb', 'name_en', 'position_uz', 'position_ru', 'position_uzb',
                     'position_en',
                     'place_uz', 'place_ru', 'place_uzb', 'place_en', ]

    form = InternForm
    inlines = [InternPhotoAdmin]
    # summernote_fields = ['biography', 'biography_uz',
    #                      'biography_ru', 'biography_uzb', 'biography_en']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


admin.site.register(Intern, InternAdmin)
