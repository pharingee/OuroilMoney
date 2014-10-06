from django.contrib import admin
# Register your models here.
from ouroilmoney.apps.reports.models import AnnualBudgetReport
from ouroilmoney.apps.reports.models import ConfirmReport


class ConfirmReportInline(admin.TabularInline):
    model = ConfirmReport
    extra = 4


class ConfirmReportAdmin(admin.ModelAdmin):

        fieldsets = (
            (None, {
                'fields': (('title', 'annual_budget_report', 'date'),
                           'summary')
            }),

            (None, {
                'fields': (('source_of_report', 'source_url'), 'is_published')
            })
        )

        list_display = ('title', 'date', 'is_published')


class AnnualBudgetReportAdmin(admin.ModelAdmin):

        fieldsets = (
            (None, {
                'fields': (('title', 'date'), 'summary')
            }),

            (None, {
                'fields': (('source_of_report', 'source_url'), 'is_published')
            })

        )

        list_display = ('title', 'date', 'is_published')
        inlines = [ConfirmReportInline, ]


admin.site.register(AnnualBudgetReport, AnnualBudgetReportAdmin)
admin.site.register(ConfirmReport, ConfirmReportAdmin)
