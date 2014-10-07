from rest_framework import viewsets
from ouroilmoney.apps.reports.models import AnnualBudgetReport
from ouroilmoney.apps.reports.models import ConfirmReport
from ouroilmoney.apps.reports.api.serializers import (
    AnnualBudgetReportSerializer, OtherReportSerializer,
    ReportSerializer)


class AnnualBudgetReportViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = AnnualBudgetReport.objects.exclude(is_published=False)
    serializer_class = AnnualBudgetReportSerializer


class OtherReportViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ConfirmReport.objects.exclude(is_published=False)
    serializer_class = OtherReportSerializer


class ReportViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = AnnualBudgetReport.objects.exclude(is_published=False)
    serializer_class = ReportSerializer
