from rest_framework import viewsets
from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue
from ouroilmoney.apps.revenues.api.serializers import (
    AnnualBudgetRevenueSerializer,
    RevenueTitleSerializer)


class AnnualBudgetRevenueViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = AnnualBudgetReportRevenue.objects.exclude(
        is_published=False).order_by('title')
    lookup_field = 'title'
    serializer_class = AnnualBudgetRevenueSerializer


class RevenueTitleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnnualBudgetReportRevenue.objects.values('title').distinct()
    serializer_class =  RevenueTitleSerializer
