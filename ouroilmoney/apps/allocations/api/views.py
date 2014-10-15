from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from ouroilmoney.apps.allocations.models import (
    AnnualBudgetAllocation,
    ConfirmAllocation)

from ouroilmoney.apps.allocations.api.serializers import (
    AnnualBudgetAllocationSerializer,
    ConfirmAllocationSerializer)


class AnnualBudgetAllocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnnualBudgetAllocation.objects.exclude(
        is_published=False).order_by('title')
    serializer_class = AnnualBudgetAllocationSerializer

    @list_route(methods=["get"])
    def titles(self, request):
        title = AnnualBudgetAllocation.objects.values_list(
            'title', flat=True).order_by('title').distinct('title')
        return Response(title)


class ConfirmAllocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConfirmAllocation.objects.exclude(
        is_published=False).order_by('annual_budget_allocation__title')
    serializer_class = ConfirmAllocationSerializer
