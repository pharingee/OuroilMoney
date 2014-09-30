from django.contrib import admin

# Register your models here.


from ouroilmoney.apps.revenues.models import  Revenue



class RevenueAdmin(admin.ModelAdmin):
        fields = ['year','report', 'title', 'amount']





admin.site.register(Revenue, RevenueAdmin)