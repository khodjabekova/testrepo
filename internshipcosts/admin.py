import datetime
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import CostStatement, CostStatementType, FinancialReport, InternUser, InternshipCostsInfo, InternshipExpenses
from django.http import HttpResponse
from django.urls import path
from .excel_utils import WriteToExcel, InternshipExpensesExcel


class CostStatementTypeAdmin(admin.ModelAdmin):
    list_display = ['name_uz', 'name_uzb', 'name_ru', 'name_en']
    exclude = ('name',)


class InternUserAdmin(admin.ModelAdmin):
    ordering = ('-created_at', )
    list_display = ['full_name', 'education',
                    'region', 'status', 'created_at', ]
    list_filter = ['status', 'education', 'region', ]
    search_fields = ['lastname', 'firstname', 'patronymic', 'phone', 'email']

    fields = ['lastname', 'firstname', 'patronymic', 'phone', 'email',
              'gender', 'citizenship', 'pnfl', 'passport_no', 'date_of_birth',
              'region', 'address', 'photo', 'work', 'work_address', 'work_region',
              'education', 'specialization', 'diplom', 'phd_diplom', 'ielts']

    exclude = (
        'updated_at',
        'lang',
        'updated_by',
    )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('report/', self.report, name='report'),
        ]
        return my_urls + urls

    def report(self, request):
        # response = HttpResponse(content_type='application/vnd.ms-excel')
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment;filename=stajorlar.xlsx'
        xlsx_data = WriteToExcel()
        response.write(xlsx_data)
        return response

    def full_name(self, obj):
        return f"{obj.lastname} {obj.firstname} {obj.patronymic}"

    full_name.short_description = "To‘liq ismi"

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        if 'accept' in request.POST.keys():
            obj.status = 2
        elif 'reject' in request.POST.keys():
            obj.status = 3
            obj.reason = request.POST['reason']

        return super().save_model(request, obj, form, change)

    def change_view(self, request, object_id, form_url="", extra_context=None):

        if object_id:
            application = InternUser.objects.get(pk=object_id)
            if not extra_context:
                extra_context = dict()
            if application.status == 1:
                extra_context['new'] = True
            # if application.status == 2:
            #     extra_context['accepted'] = True

        return super(InternUserAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)


class CostStatementInline(admin.TabularInline):
    model = CostStatement
    extra = 1
    fields = ['type', 'days', 'currency',
              'cost', 'note', 'link', 'screenshot']
    verbose_name = 'Xarajatlar asosnomasi'
    verbose_name_plural = 'Xarajatlar asosnomasi'
    # readonly_fields = ('type', 'days', 'currency',
    #           'cost', 'note', 'link', 'screenshot')


class InternshipExpensesAdmin(admin.ModelAdmin):
    ordering = ('-created_at', )
    list_display = ['intern', 'created_at', 'status', ]
    list_filter = ['status', ]
    inlines = [CostStatementInline]
    readonly_fields = ('intern',)
    exclude = (
        'slug',
        'is_active',
        'status',
        'created_by',
        'updated_by',
    )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<path:object_id>/cost-statements/', self.cost_statements,
                 name='internshipcosts_internshipexpenses_report'),
        ]
        return my_urls + urls

    def cost_statements(self, request, object_id, *args, **kwargs):
        # response = HttpResponse(content_type='application/vnd.ms-excel')
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment;filename=xarajatlar_asosnomasi.xlsx'

        xlsx_data = InternshipExpensesExcel(object_id=object_id)

        response.write(xlsx_data)
        return response

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        if 'accept' in request.POST.keys():
            obj.status = 2
        elif 'reject' in request.POST.keys():
            obj.status = 3
            obj.reason = request.POST['reason']

        return super().save_model(request, obj, form, change)

    def change_view(self, request, object_id, form_url="", extra_context=None):

        if object_id:
            application = InternshipExpenses.objects.get(pk=object_id)
            if not extra_context:
                extra_context = dict()
            if application.status == 1:
                extra_context['new'] = True

        return super(InternshipExpensesAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)


class FinancialReportAdmin(admin.ModelAdmin):
    ordering = ('-created_at', )
    list_display = ['intern', 'created_at', 'status', ]
    list_filter = ['status', ]
    readonly_fields = ('intern', 'file')

    exclude = (
        'slug',
        'is_active',
        'status',
        'created_by',
        'updated_by',
    )

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        if 'accept' in request.POST.keys():
            obj.status = 2
        elif 'reject' in request.POST.keys():
            obj.status = 3
            obj.reason = request.POST['reason']

        return super().save_model(request, obj, form, change)

    def change_view(self, request, object_id, form_url="", extra_context=None):

        if object_id:
            obj = FinancialReport.objects.get(pk=object_id)
            if not extra_context:
                extra_context = dict()
            if obj.status == 1:
                extra_context['new'] = True

        return super(FinancialReportAdmin, self).change_view(request, object_id, form_url=form_url, extra_context=extra_context)


class InternshipCostsInfoAdmin(SingletonModelAdmin):

    exclude = (
        'cost_statement',
        'financial_report',
        'created_by',
        'updated_by',
    )

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.updated_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(InternUser, InternUserAdmin)
admin.site.register(InternshipExpenses, InternshipExpensesAdmin)
admin.site.register(FinancialReport, FinancialReportAdmin)
admin.site.register(CostStatementType, CostStatementTypeAdmin)
admin.site.register(InternshipCostsInfo, InternshipCostsInfoAdmin)
