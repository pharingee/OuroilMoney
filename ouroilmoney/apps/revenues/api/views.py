from rest_framework import viewsets
from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue
from ouroilmoney.apps.revenues.api.serializers import (
    AnnualBudgetRevenueSerializer,)


class AnnualBudgetRevenueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnnualBudgetReportRevenue.objects.exclude(
        is_published=False).order_by('title')
    serializer_class = AnnualBudgetRevenueSerializer
