
from django.contrib import admin
from django.db import models
from django import forms
from tinymce.widgets import TinyMCE
from solo.admin import SingletonModelAdmin

from .models import AppealQuarterDetailStatistics, AppealQuarterStatistics, AppealStatistics, Country, CountryStatistics, EquipmentPurchaseStatistics, FinanceInternshipStatistics, FinanceInternshipYear, ScienceField, Region, RegionStatistics, FinanceEntity, InternCount, \
    RegionSight, RegionSightImages, YoungScientistInternship, ScientificInternship, ScientificInternshipStatistic, \
    AnnualCost, NormativeDocument


class ScienceFieldAdmin(admin.ModelAdmin):
    list_display = ["name_uz", 'name_ru', 'index']

    exclude = (
        'name',
        'slug',
        'created_by',
        'updated_by'
    )
    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request) -> bool:
        count = ScienceField.objects.all().count() 
        if count < 10:
            return True
        else:
            return False

class CountryStatisticsAdmin(admin.TabularInline):
    model = CountryStatistics
    extra = 1
    fields = ['is_active', 'science_field', 'count']
    verbose_name = "Statistika"
    verbose_name_plural = "Statistikalar"


class CountryAdmin(admin.ModelAdmin):
    list_display = ["name_uz", 'name_uzb', 'name_ru', 'name_en']

    exclude = (
        'name',
        'slug',
        'created_by',
        'updated_by'
    )

    inlines = [CountryStatisticsAdmin]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


class RegionStatisticsAdmin(admin.TabularInline):
    model = RegionStatistics
    extra = 1
    fields = ['is_active', 'science_field', 'count']
    verbose_name = "Statistika"
    verbose_name_plural = "Statistikalar"


class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']

    exclude = (
        'slug',
        'created_by',
        'updated_by'
    )

    inlines = [RegionStatisticsAdmin]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


class FinanceEntityAdmin(admin.ModelAdmin):
    fields = ['type', "year", "sum"]
    list_display = ['type', "year", "sum", "is_active"]
    list_filter = ['type', "year", "is_active"]
    search_fields = ['type', "year", "sum",]
    exclude = (
        "slug",
        "created_by",
        "updated_by",
    )

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


class InternCountAdmin(admin.ModelAdmin):
    fields = ["is_active", 'year', "count"]
    list_display = ["year", "count"]
    exclude = (
        "slug",
        "created_by",
        "updated_by",
    )

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


class RegionSightImageAdmin(admin.TabularInline):
    model = RegionSightImages
    extra = 1
    verbose_name = 'Rasm'
    verbose_name_plural = "Rasmlar"

    formfield_overrides = {
        models.ImageField: {'widget': forms.ClearableFileInput(attrs={'multiple': True})},
    }


class RegionSightForm(forms.ModelForm):
    content_uz = forms.CharField(label='Matn [uz]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    content_uzb = forms.CharField(label='Matn [uzb]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_ru = forms.CharField(label='Matn [ru]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)
    content_en = forms.CharField(label='Matn [en]', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), required=False)

    class Meta:
        model = RegionSight
        exclude = (
            'title',
            'content',
            'slug',
            'created_by',
            'updated_by'
        )


class RegionSightAdmin(admin.ModelAdmin):
    inlines = [RegionSightImageAdmin]
    list_display = ['slug', 'title', 'content', 'region', 'image']

    form = RegionSightForm

    # summernote_fields = ['content_uz', 'content_ru', 'content_uzb', 'content_en']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    def delete_selected(self, request, obj):
        for o in obj:
            o.delete()

    delete_selected.short_description = "O'chirish"


class YoungScientistInternshipAdmin(admin.ModelAdmin):
    list_display = ['scientist', 'country', 'field', 'relation']
    exclude = (
        'created_by',
        'updated_by',
    )

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request) -> bool:
        count = YoungScientistInternship.objects.all().count() 
        if count < 1:
            return True
        else:
            return False


    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    def delete_selected(self, request, obj):
        for o in obj:
            o.delete()

    delete_selected.short_description = "O'chirish"


class ScientificInternshipStatisticAdmin(admin.TabularInline):
    model = ScientificInternshipStatistic
    extra = 1
    exclude = (
        'is_active',
        'created_by',
        'updated_by',
    )


class ScientificInternshipAdmin(admin.ModelAdmin):
    list_display = ['year', 'region', 'successful', 'rejected']
    list_filter = ['year', 'region']
    exclude = (
        'created_by',
        'updated_by'
    )
    inlines = [ScientificInternshipStatisticAdmin]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


class FinanceInternshipStatisticsAdmin(admin.TabularInline):
    model = FinanceInternshipStatistics
    extra = 1
    exclude = (
        'is_active',
        'slug',
        'created_by',
        'updated_by',
    )


class FinanceInternshipYearAdmin(admin.ModelAdmin):
    list_display = ('year',)
    list_filter = ('year', )
    exclude = (
        'slug',
        'created_by',
        'updated_by'
    )
    inlines = [FinanceInternshipStatisticsAdmin]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

class AnnualCostAdmin(admin.ModelAdmin):
    list_display = ['year', 'fields', 'cost']
    exclude = (
        'created_by',
        "updated_by"
    )

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    def delete_selected(self, obj):
        for o in obj:
            o.delete()

    delete_selected.short_description = "O'chirish"


class NormativeDocumentAdmin(admin.ModelAdmin):
    list_display = ["date", 'count', 'is_active']
    exclude = ['created_by', 'updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)

    def delete_selected(self, obj):
        for o in obj:
            o.delete()

    delete_selected.short_description = "O'chirish"
class AppealStatisticsAdmin(SingletonModelAdmin):
    exclude = (
        'slug',
        'created_by',
        'updated_by',
    )

class AppealQuarterDetailAdmin(admin.TabularInline):
    model = AppealQuarterDetailStatistics
    verbose_name = "Murojaatlar statistikasi"
    verbose_name_plural = "Murojaatlar statistikasi"
    extra = 1
    exclude = (
        'is_active',
        'slug',
        'created_by',
        'updated_by',
    )
class AppealQuarterStatisticsAdmin(admin.ModelAdmin):
    exclude = (
        'slug',
        'created_by',
        'updated_by',
    )
    inlines = [AppealQuarterDetailAdmin]

class EquipmentStatisticsForm(forms.ModelForm):
    class Meta:
        model = EquipmentPurchaseStatistics
        exclude = (
        'slug',
        'title',
        'created_by',
        'updated_by',
        )
        widgets = {
            'title_uz': forms.Textarea(attrs={'cols': 100, 'rows': 3}),
            'title_uzb': forms.Textarea(attrs={'cols': 100, 'rows': 3}),
            'title_ru': forms.Textarea(attrs={'cols': 100, 'rows': 3}),
            'title_en': forms.Textarea(attrs={'cols': 100, 'rows': 3}),
        }

class EquipmentStatisticsAdmin(admin.ModelAdmin):
    list_display = ["title", 'equipment_count', 'invested', 'is_active']

    # form = EquipmentStatisticsForm
    exclude = (
        'slug',
        'title',
        'created_by',
        'updated_by',
    )


admin.site.register(Country, CountryAdmin)
admin.site.register(ScienceField, ScienceFieldAdmin)
admin.site.register(FinanceEntity, FinanceEntityAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(InternCount, InternCountAdmin)
admin.site.register(RegionSight, RegionSightAdmin)
admin.site.register(YoungScientistInternship, YoungScientistInternshipAdmin)
admin.site.register(ScientificInternship, ScientificInternshipAdmin)
admin.site.register(AnnualCost, AnnualCostAdmin)
admin.site.register(NormativeDocument, NormativeDocumentAdmin)
admin.site.register(AppealStatistics, AppealStatisticsAdmin)
admin.site.register(AppealQuarterStatistics, AppealQuarterStatisticsAdmin)
admin.site.register(EquipmentPurchaseStatistics, EquipmentStatisticsAdmin)
admin.site.register(FinanceInternshipYear, FinanceInternshipYearAdmin)
