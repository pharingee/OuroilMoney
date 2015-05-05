from django.contrib import admin

# Register your models here.
from ouroilmoney.apps.liftings.models import Lifting


@admin.register(Lifting)
class LiftingAdmin(admin.ModelAdmin):
    list_display = (
        'report', 'date',
        'volume_of_lifting', 'price', 'partner', 'field',
        'lifting_proceed', 'is_published', 'lifting_has_receipt')

    fields = [
        'report', 'date', 'volume_of_lifting', 'partner', 'field',
        'selling_price', 'lifting_proceed', 'lifting_receipt', 'is_published']

    list_filter = ('report', 'volume_of_lifting', 'partner', 'field', 'selling_price', 'date', 'is_published')
