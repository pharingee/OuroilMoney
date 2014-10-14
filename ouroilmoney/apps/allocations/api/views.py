from rest_framework import viewsets
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


class ConfirmAllocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConfirmAllocation.objects.exclude(
        is_published=False).order_by('annual_budget_allocation__title')
    serializer_class = ConfirmAllocationSerializer
