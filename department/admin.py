from django.contrib import admin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django import forms
from .models import Department, Employee, SupervisoryBoard
from tinymce.widgets import TinyMCE
from mptt.admin import MPTTModelAdmin


class EmployeeForm(forms.ModelForm):
    biography_uz = forms.CharField(label='Tarjimai hol [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    biography_uzb = forms.CharField(label='Tarjimai hol [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    biography_ru = forms.CharField(label='Tarjimai hol [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    biography_en = forms.CharField(label='Tarjimai hol [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    responsibilities_uz = forms.CharField(label="Majburiyatlari [uz]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    responsibilities_uzb = forms.CharField(label="Majburiyatlari [uzb]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    responsibilities_ru = forms.CharField(label="Majburiyatlari [ru]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    responsibilities_en = forms.CharField(label="Majburiyatlari [en]", widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)

    class Meta:
        model = Employee
        exclude = (
            'slug',
            'name',
            'position',
            'biography',
            'working_hours',
            'responsibilities',
            'created_by',
            'updated_by',
        )
        widgets={
            'department': forms.Select(attrs={'class': 'bootstrap-select', 'data-width':"80%"})
            }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = (
        'created_by',
        'updated_by',
        'name',
        'slug',
    )
        widgets={
            'parent': forms.Select(attrs={'class': 'bootstrap-select', 'data-width':"80%"})
            }

class DepartmentAdmin(MPTTModelAdmin):
    list_display = ('name_uz', 'index')
    form = DepartmentForm
    exclude = (
        'created_by',
        'updated_by',
        'name',
        'slug',
    )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name_uz', 'name_uzb', 'name_ru', 'name_en', ]
    list_filter = ['is_chief', 'department']
    form = EmployeeForm
    exclude = (
        'slug',
        'name',
        'position',
        'biography',
        'working_hours',
        'responsibilities',
        'created_by',
        'updated_by',
    )

    def add_view(self, request, form_url='', extra_context=None):
        if request.POST:
            chief = request.POST['is_chief'] if 'is_chief' in request.POST.keys(
            ) else None
            department_id = request.POST['department'] if 'department' in request.POST.keys(
            ) else None
            empl = Employee.objects.filter(
                department__id=department_id, is_chief=True)
            if chief == 'on' and empl:
                self.message_user(
                    request, "Bu bo'limning boshlig'i bor!", level=messages.ERROR)
                return HttpResponseRedirect(form_url)
        return super().add_view(request, form_url, extra_context)



    def change_view(self, request, object_id, form_url="", extra_context=None):
        if request.POST:
            chief = request.POST['is_chief'] if 'is_chief' in request.POST.keys(
            ) else None
            department_id = request.POST['department'] if 'department' in request.POST.keys(
            ) else None
            empl = Employee.objects.filter(
                department__id=department_id, is_chief=True)
            current = empl.filter(id=object_id).exists()
            if chief == 'on' and empl and not current:
                self.message_user(
                    request, "Bu bo'limning boshlig'i bor!", level=messages.ERROR)
                return HttpResponseRedirect(form_url)
        return super().change_view(request, object_id, form_url, extra_context)


class SupervisoryBoardAdmin(admin.ModelAdmin):
    list_display = ['name_uz', 'name_uzb', 'name_ru', 'name_en', 'index']

    exclude = (
        'created_by',
        'updated_by',
        'name',
        'slug',
        'position',
    )


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(SupervisoryBoard, SupervisoryBoardAdmin)
