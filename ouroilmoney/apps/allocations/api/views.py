from rest_framework import viewsets
from ouroilmoney.apps.allocations.models import (
    AnnualBudgetAllocation,
    ConfirmAllocation)

from ouroilmoney.apps.allocations.api.serializers import (
    AnnualBudgetAllocationSerializer,
    ConfirmAllocationSerializer)


class AnnualBudgetAllocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnnualBudgetAllocation.objects.exclude(is_published=False)
    serializer_class = AnnualBudgetAllocationSerializer


class ConfirmAllocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConfirmAllocation.objects.exclude(is_published=False)
    serializer_class = ConfirmAllocationSerializer
