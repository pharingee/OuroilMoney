from django.contrib import admin

# Register your models here.


from ouroilmoney.apps.revenues.models import  Revenues



class RevenuesAdmin(admin.ModelAdmin):
        fields = ['year','report', 'title', 'amount']





admin.site.register(Revenues, RevenuesAdmin)