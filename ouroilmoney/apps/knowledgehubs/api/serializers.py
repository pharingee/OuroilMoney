from rest_framework import serializers
from ouroilmoney.apps.knowledgehubs.models import KnowledgeHub


class KnowledgeHubSerializer(serializers.ModelSerializer):
    document_url = serializers.Field(source='get_document')

    class Meta:
        model = KnowledgeHub
        fields = (
            'id', 'created',
            'document_url',
            'is_published',
            'title', 'date')
