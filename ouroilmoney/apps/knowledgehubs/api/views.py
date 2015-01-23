from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
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

    @list_route(methods=["get"])
    def piacs(self, request):
        """
        Get all documents tagged as piac
        """
        piac = KnowledgeHub.objects.filter(category="PIAC")
        serializer = KnowledgeHubSerializer(piac, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def governments(self, request):
        """
        Get all documents tagged as government.
        """
        government = KnowledgeHub.objects.filter(
            category="GOVERNMENT").exclude(is_published=False)
        serializer = KnowledgeHubSerializer(government, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def civil_societies(self, request):
        """
        Get all documents tagged as civil societies
        """
        civil_societies = KnowledgeHub.objects.filter(
            category="CIVIL SOCIETY").exclude(is_published=False)
        serializer = KnowledgeHubSerializer(civil_societies, many=True)
        return Response(serializer.data)
