from django.contrib import admin

# Register your models here.


from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue


@admin.register(AnnualBudgetReportRevenue)
class AnnualBudgetReportRevenueAdmin(admin.ModelAdmin):
        fields = ['year', 'report', 'title', 'amount', 'is_published']
        list_display = ('title', 'revenue_amount', 'year', 'is_published')
