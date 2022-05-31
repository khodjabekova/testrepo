from django.contrib import admin, messages
from django.http import HttpResponseRedirect

from gallery.models import PhotoGalleryImages, PhotoGallery, VideoGallery


class PhotoGalleryImagesAdmin(admin.TabularInline):
    model = PhotoGalleryImages
    extra = 1
    verbose_name = 'Rasm'
    verbose_name_plural = "Rasmlar"
    
    def has_delete_permission(self, request, obj):
        return True

    # formfield_overrides = {
    #     models.ImageField: {"widget": forms.ClearableFileInput(attrs={'multiple': True})},
    # }


class PhotoGalleryAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)
    exclude = ('name', 'created_by', 'updated_by', 'slug')
    list_display = ("slug", "name_uz", "index", 'created_by')
    search_fields = ("name_uz", "name_ru", "name_uzb", "name_en")
    inlines = [PhotoGalleryImagesAdmin]
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

        # for filename, file in request.FILES.items():
        #     if filename == "cover":
        #         continue
        #     pictures = request.FILES.getlist(filename)
        #     for picture in pictures:
        #         PhotoGalleryImages.objects.create(gallery=obj, image=picture)
        # return super(PhotoGalleryAdmin, self).save_model(request, obj, form, change)


admin.site.register(PhotoGallery, PhotoGalleryAdmin)


class VideoGalleryAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_display = ["name_uz", "name_ru", "name_uzb", "name_en"]
    search_fields = ['name']
    exclude = ['name', 'slug', 'created_by', "updated_by"]

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        gallery = VideoGallery.objects.get(id=object_id)
        extra_context["form"] = self.get_form(request=request, obj=gallery)
        if request.POST:
            forms_count = int(request.POST['video_list-TOTAL_FORMS'])
            video_count = 0
            for i in range(forms_count):
                link_key = 'video_list-{0}-link'.format(i)
                link = request.POST.get(link_key, False)
                delete_key = 'video_list-{0}-DELETE'.format(i)
                has_delete = request.POST.get(delete_key, False)
                if link != '' and (not has_delete or (has_delete and has_delete != 'on')):
                    video_count = video_count + 1
            if video_count == 0:
                self.message_user(
                    request, "Kamida bitta video bo'lishi kerak!", level=messages.ERROR)
                return HttpResponseRedirect(form_url)
            else:
                return super(VideoGalleryAdmin, self).change_view(request, object_id, form_url=form_url,
                                                                  extra_context=extra_context)
        else:
            return super(VideoGalleryAdmin, self).change_view(request, object_id, form_url=form_url,
                                                              extra_context=extra_context)

    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            o.delete()

    delete_selected.short_description = "O'chirish"

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(VideoGallery, VideoGalleryAdmin)
