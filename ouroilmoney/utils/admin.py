from django.contrib import admin
from ouroilmoney.utils.models import Region


# Register your models here.

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    fields = ['region']
