from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from ouroilmoney.apps.revenues.models import AnnualBudgetReportRevenue
from ouroilmoney.apps.revenues.api.serializers import (
    AnnualBudgetRevenueSerializer,)



class AnnualBudgetRevenueViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = AnnualBudgetReportRevenue.objects.exclude(
        is_published=False).order_by('title')
    serializer_class = AnnualBudgetRevenueSerializer

    @list_route(methods=["get"])
    def titles(self, request):
        title=AnnualBudgetReportRevenue.objects.values('title').order_by('title').distinct('title')
        return  Response(title)

