from django.contrib import admin
from ouroilmoney.utils.models import Region, SmsMessage, Ministry, Partner, Field, SubCategory


# Register your models here.

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    fields = ['region']


@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    fields = ['ministry']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fields = ['partner', 'is_published']
    list_display = ('partner', 'is_published')


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    fields = ['field', 'is_published']
    list_display = ('field', 'is_published')


@admin.register(SmsMessage)
class SmsCommentAdmin(admin.ModelAdmin):
    fields = ['message', 'user', 'status']
    list_display = (
        'user',
        'message',
        'status')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    fields = ['subcategory', 'is_published']
    list_display = (
        'subcategory',
        'is_published')
