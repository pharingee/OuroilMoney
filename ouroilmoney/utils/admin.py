from django.contrib import admin
from ouroilmoney.utils.models import Region,SmsMessage


# Register your models here.

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    fields = ['region']




@admin.register(SmsMessage)
class SmsCommentAdmin(admin.ModelAdmin):
    fields = ['message', 'user', 'status']
    list_display = (
        'user',
        'message',
        'status')