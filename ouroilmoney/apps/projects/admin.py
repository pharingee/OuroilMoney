from django.contrib import admin

# Register your models here.
from ouroilmoney.apps.projects.models import AnnualBudgetSector
from ouroilmoney.apps.projects.models import ConfirmSector
from ouroilmoney.apps.projects.models import AnnualBudgetProject
from ouroilmoney.apps.projects.models import ConfirmProject


@admin.register(AnnualBudgetSector)
class AnnualBudgetSectorAdmin(admin.ModelAdmin):
    fields = ['title', 'total_amount', 'allocation']
    list_display = ( 'allocation','title', 'amount')


@admin.register(ConfirmSector)
class ConfirmSectorAdmin(admin.ModelAdmin):
    fields = [ 'total_amount', 'allocation','annual_budget_sector']
    list_display = ('allocation','annual_budget_sector', 'amount_annual_budget', 'amount_another_report',)




@admin.register(AnnualBudgetProject)
class AnnualBudgetProjectAdmin(admin.ModelAdmin):
     fields= ['name','sector', 'amount']
     list_display = ('name', 'sector' ,'amount_from_annual_project')

@admin.register(ConfirmProject)
class ConfirmProjectAdmin(admin.ModelAdmin):
     fields= ['sector', 'amount','project']
     list_display = ('sector' ,'amount_from_other_project', 'amount_from_annual_project')