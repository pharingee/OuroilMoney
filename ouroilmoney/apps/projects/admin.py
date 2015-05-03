from django.contrib import admin

# Register your models here.
from ouroilmoney.apps.projects.models import AnnualBudgetSector
from ouroilmoney.apps.projects.models import ConfirmSector
from ouroilmoney.apps.projects.models import AnnualBudgetProject
from ouroilmoney.apps.projects.models import ConfirmProject



@admin.register(AnnualBudgetSector)
class AnnualBudgetSectorAdmin(admin.ModelAdmin):
    fields = ['title', 'amount', 'allocation', 'expenditure' ,'currency','is_published']
    list_display = ('allocation' ,'title','expenditure', 'amount_from_annual_budget','is_published')
    list_filter = ('allocation', 'title','expenditure', 'currency','is_published')


@admin.register(ConfirmSector)
class ConfirmSectorAdmin(admin.ModelAdmin):
    fields = ['amount', 'allocation', 'annual_budget_sector','currency','is_published']
    list_display = ('allocation','annual_budget_sector', 'amount_from_annual_budget', 'amount_another_report','is_published')
    list_filter = ('allocation','currency', 'is_published')



@admin.register(AnnualBudgetProject)
class AnnualBudgetProjectAdmin(admin.ModelAdmin):
     fields= ['title','sector','regions','ministry','amount','town','currency','is_published']
     list_display = ('title', 'sector' ,'ministry','amount_from_annual_project','town','is_published')
     list_filter  = ('title','sector', 'ministry','town','currency','is_published')

@admin.register(ConfirmProject)
class ConfirmProjectAdmin(admin.ModelAdmin):
     fields= ['image','video','amount','ministry','sector','regions', 'project','town','remarks','currency', 'is_published']
     list_display = ('sector' ,'admin_image','ministry','amount_from_other_project', 'amount_from_annual_project','town','remarks','is_published')
     list_filter  = ('sector','town','ministry','is_published','remarks','currency')
