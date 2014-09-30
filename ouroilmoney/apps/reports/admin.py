from django.contrib import admin
# Register your models here.
from ouroilmoney.apps.reports.models import Report


class ReportAdmin(admin.ModelAdmin):
        fields = [
            'title', 'report_type', 'date', 'source_of_report', 'source_url']

admin.site.register(Report, ReportAdmin)
