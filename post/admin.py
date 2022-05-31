from django import forms
from django.contrib import admin
from .models import Post, PostAttachments, PostImages
from tinymce.widgets import TinyMCE
from mptt.admin import MPTTModelAdmin

class PostImagesAdmin(admin.TabularInline):
    model = PostImages
    extra = 1
    verbose_name = 'Post Rasmi'
    verbose_name_plural = 'Post Rasmlari'


class PostAttachmentsAdmin(admin.TabularInline):
    model = PostAttachments
    extra = 1
    exclude = ['name', 'file']
    verbose_name = 'Fayl'
    verbose_name_plural = "Fayllar"

class PostForm(forms.ModelForm):
    content_uz = forms.CharField(label='Matn [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    content_uzb = forms.CharField(label='Matn [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}),required=False)
    content_ru = forms.CharField(label='Matn [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_en = forms.CharField(label='Matn [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    class Meta:
        model = Post
        exclude = ['name', 'created_by', 'updated_by',
               'slug', 'views', 'title', 'content']
        widgets={
            'menu': forms.Select(attrs={'class': 'bootstrap-select', 'data-width':"80%"})
            }

class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    ordering = ('-pub_date',)
    form = PostForm

    list_filter = ['menu', 'is_active', ]
    list_display = ['title_uz', 'menu', 'pub_date', 'is_active',]
    search_fields = ['title_ru', 'title_uz', 'title_uzb', 'title_en',
                     'content_uz', 'content_uzb', 'content_ru', 'content_en']
    exclude = ['name', 'created_by', 'updated_by',
               'slug', 'views', 'title', 'content']

    inlines = [PostImagesAdmin, PostAttachmentsAdmin]
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
                PostImages.objects.create(post=obj, image=picture)
        return super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
