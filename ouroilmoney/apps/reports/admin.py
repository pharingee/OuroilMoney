from django.contrib import admin
# Register your models here.
from ouroilmoney.apps.reports.models import (
    AnnualBudgetReport,
    ConfirmReport,
    CalendarOfReport)


class ConfirmReportInline(admin.TabularInline):
    model = ConfirmReport
    extra = 4


class ConfirmReportAdmin(admin.ModelAdmin):

        fieldsets = (
            (None, {
                'fields': ((
                    'title', 'annual_budget_report', 'date', 'report_type'),
                    'summary')
            }),

            (None, {
                'fields': (('source_of_report', 'source_url'), 'is_published')
            })
        )

        list_display = (
            'title',
            'report_type',
            'date',
            'is_published',
            'report_has_document')

        list_filter = (
            'date',
            'is_published',
            'title')


class AnnualBudgetReportAdmin(admin.ModelAdmin):

        fieldsets = (
            (None, {
                'fields': (('title', 'date'), 'summary')
            }),

            (None, {
                'fields': (
                    ('source_of_report', 'source_url'),
                    'is_published', 'document')
            })

        )

        list_display = ('title', 'date', 'is_published', 'report_has_document')
        list_filter = ('date', 'is_published', 'title')
        inlines = [ConfirmReportInline, ]


class CalendarOfReportAdmin(admin.ModelAdmin):

        fieldsets = (
            (None, {
                'fields': (('title', 'date'), 'summary', 'is_published')
            }),

        )

        list_display = ('title', 'date', 'is_published', 'summary')
        list_filter = ('date', 'is_published', 'title', 'date')


admin.site.register(CalendarOfReport, CalendarOfReportAdmin)
admin.site.register(AnnualBudgetReport, AnnualBudgetReportAdmin)
admin.site.register(ConfirmReport, ConfirmReportAdmin)
