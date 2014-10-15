from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from ouroilmoney.apps.reports.models import AnnualBudgetReport
from ouroilmoney.apps.reports.models import ConfirmReport
from ouroilmoney.apps.reports.api.serializers import (
    AnnualBudgetReportSerializer, OtherReportSerializer,
    ReportSerializer)


class AnnualBudgetReportViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = AnnualBudgetReport.objects.exclude(is_published=False)
    serializer_class = AnnualBudgetReportSerializer

    @list_route(methods=["get"])
    def titles(self, request):
        title = AnnualBudgetReport.objects.values_list(
            'title', flat=True).order_by('title').distinct('title')
        return Response(title)


class OtherReportViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ConfirmReport.objects.exclude(is_published=False)
    serializer_class = OtherReportSerializer


class ReportViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = AnnualBudgetReport.objects.exclude(is_published=False)
    serializer_class = ReportSerializer
