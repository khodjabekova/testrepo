from django import forms
from django.contrib import admin
from .models import Menu
from mptt.admin import MPTTModelAdmin

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        exclude = (
            'id',
            'slug',
            'title',
            'note',
            'created_by',
            'updated_by',
        )
        widgets={
            'parent': forms.Select(attrs={'class': 'bootstrap-select', 'data-width':"80%"})
            }

class MenuAdmin(MPTTModelAdmin):
    list_display = ['title_uz', 'index', ]
    search_fields = ['title_uz', 'title_uzb', 'title_ru', 'title_en', 'note']
    form = MenuForm
    exclude = (
        'id',
        'slug',
        'title',
        'note',
        'created_by',
        'updated_by',
    )   



    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


    current_object = None

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.current_object = obj.id
        else:
            self.current_object = None
        return super(MenuAdmin, self).get_form(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            if self.current_object:
                current = Menu.objects.get(pk=self.current_object)
                descendant = current.get_descendants(include_self=True)
                kwargs["queryset"] = Menu.objects.all().exclude(id__in=descendant)
            else:
                kwargs["queryset"] = Menu.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Menu, MenuAdmin)
