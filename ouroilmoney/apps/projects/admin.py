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
     fields= ['title','sector', 'amount','region','currency','is_published']
     list_display = ('title', 'sector' ,'amount_from_annual_project','region','is_published')
     list_filter  = ('title','sector', 'region','currency','is_published')

@admin.register(ConfirmProject)
class ConfirmProjectAdmin(admin.ModelAdmin):
     fields= ['image','amount','sector', 'project','region','remarks','currency','is_published']
     list_display = ('sector' ,'admin_image','amount_from_other_project', 'amount_from_annual_project','region','remarks','is_published')
     list_filter  = ('sector', 'region','is_published','remarks','currency')
