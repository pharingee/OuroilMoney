from django.contrib import admin
from ouroilmoney.apps.allocations.models import (
    AnnualBudgetAllocation, ConfirmAllocation)

# Register your models here.


@admin.register(ConfirmAllocation)
class ConfirmAllocationAdmin(admin.ModelAdmin):
    fields = [
        'annual_budget_allocation',
        'report',
        'currency',
        'amount',
        'is_published']

    list_display = (
        'report',
        'currency',
        'allocated_amount',
        'annual_budget_allocation',
        'annual_budget_allocation_amount',
        'is_published')


@admin.register(AnnualBudgetAllocation)
class AllocationAdmin(admin.ModelAdmin):
    fields = ['title', 'currency', 'amount', 'report', 'is_published']

    list_display = (
        'title',
        'report',
        'currency',
        'allocated_amount',
        'is_published')
