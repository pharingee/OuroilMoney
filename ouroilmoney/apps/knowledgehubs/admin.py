from django.contrib import admin
from ouroilmoney.apps.knowledgehubs.models import KnowledgeHub


# Register your models here.
@admin.register(KnowledgeHub)
class KnowledgeHubAdmin(admin.ModelAdmin):
    fields = ['title', 'date', 'document', 'is_published']
    list_display = (
        'title',
        'date',
        'report_has_document',
        'is_published')

    list_filter = ('date', 'is_published', 'created')
