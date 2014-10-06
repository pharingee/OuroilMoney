from django.contrib import admin
from ouroilmoney.apps.allocations.models import (
    AnnualBudgetAllocation, ConfirmAllocation)

# Register your models here.


@admin.register(ConfirmAllocation)
class ConfirmAllocationAdmin(admin.ModelAdmin):
    fields = ['annual_budget_allocation', 'report', 'amount', 'is_published']
    list_display = (
        'report',
        'allocated_amount',
        'annual_budget_allocation',
        'annual_budget_allocation_amount', 'is_published')


@admin.register(AnnualBudgetAllocation)
class AllocationAdmin(admin.ModelAdmin):
    fields = ['title', 'amount', 'report', 'is_published']
    list_display = ('title', 'report', 'allocated_amount', 'is_published')
