from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue
from ouroilmoney.apps.revenues.api.serializers import (
    AnnualBudgetRevenueSerializer,)


class AnnualBudgetRevenueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Revenue Resource
    """

    queryset = AnnualBudgetReportRevenue.objects.exclude(
        is_published=False).order_by('title')
    serializer_class = AnnualBudgetRevenueSerializer

    @list_route(methods=["get"])
    def titles(self, request):
        title = AnnualBudgetReportRevenue.objects.values_list('title',flat=True).order_by('title').distinct('title')
        return Response(title)

    @list_route(methods=["get"])
    def total(self, request):
        return Response({'total': AnnualBudgetReportRevenue.revenue_objects.totalRevenue()})

