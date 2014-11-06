from django.contrib import admin

# Register your models here.
from ouroilmoney.apps.projects.models import AnnualBudgetSector
from ouroilmoney.apps.projects.models import ConfirmSector
from ouroilmoney.apps.projects.models import AnnualBudgetProject
from ouroilmoney.apps.projects.models import ConfirmProject


@admin.register(AnnualBudgetSector)
class AnnualBudgetSectorAdmin(admin.ModelAdmin):
    fields = ['title', 'amount', 'allocation','is_published']
    list_display = ('allocation', 'title', 'amount_from_annual_budget','is_published')
    list_filter = ('allocation', 'title', 'is_published')


@admin.register(ConfirmSector)
class ConfirmSectorAdmin(admin.ModelAdmin):
    fields = ['amount', 'allocation', 'annual_budget_sector','is_published']
    list_display = ('allocation','annual_budget_sector', 'amount_from_annual_budget', 'amount_another_report','is_published')
    list_filter = ('allocation', 'is_published')



@admin.register(AnnualBudgetProject)
class AnnualBudgetProjectAdmin(admin.ModelAdmin):
     fields= ['title','sector', 'amount','region','is_published']
     list_display = ('title', 'sector' ,'amount_from_annual_project','region','is_published')
     list_filter  = ('title','sector', 'region','is_published')

@admin.register(ConfirmProject)
class ConfirmProjectAdmin(admin.ModelAdmin):
     fields= ['amount','sector', 'project','region','remarks','is_published']
     list_display = ('sector' ,'amount_from_other_project', 'amount_from_annual_project','region','remarks','is_published')
     list_filter  = ('sector', 'region','is_published','remarks')
