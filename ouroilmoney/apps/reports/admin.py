from django.contrib import admin

# Register your models here.

from ouroilmoney.apps.reports.models import Reports



class ReportsAdmin(admin.ModelAdmin):
        fields= ['title', 'summary', 'report_type','date','source','source_url']



admin.site.register(Reports, ReportsAdmin)