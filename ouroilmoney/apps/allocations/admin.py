from django.contrib import admin
from ouroilmoney.apps.allocations.models import (Allocations, SubAllocations)

# Register your models here.


class AllocationsAdmin(admin.ModelAdmin):
    fields = ['title', 'amount', 'revenue']


class SubAllocationsAdmin(admin.ModelAdmin):
    fields = ['title', 'amount', 'allocation']


admin.site.register(Allocations, AllocationsAdmin)
admin.site.register(SubAllocations, SubAllocationsAdmin)
