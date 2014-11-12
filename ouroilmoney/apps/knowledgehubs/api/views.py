from rest_framework import viewsets
from ouroilmoney.apps.knowledgehubs.api.serializers import (
    KnowledgeHubSerializer)
from ouroilmoney.apps.knowledgehubs.models import (KnowledgeHub)


class KnowledgeHubViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Allocations from the annual budget Report Resource
    """
    queryset = KnowledgeHub.objects.exclude(
        is_published=False).order_by('title')
    serializer_class = KnowledgeHubSerializer
