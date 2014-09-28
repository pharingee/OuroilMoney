from django.contrib import admin

# Register your models here.
from ouroilmoney.apps.liftings.models import Liftings



class LiftingsAdmin(admin.ModelAdmin):
    fields= ['revenue','volume', 'barrel_price', 'lifting_proceed']




admin.site.register(Liftings, LiftingsAdmin)


