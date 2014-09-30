from django.contrib import admin
from ouroilmoney.apps.allocations.models import (Allocation)

# Register your models here.


class AllocationAdmin(admin.ModelAdmin):
    fields = ['title', 'amount','year']



admin.site.register(Allocation, AllocationAdmin)

