from rest_framework import viewsets
from ouroilmoney.apps.reports.models import AnnualBudgetReport
from ouroilmoney.apps.reports.api.serializers import (
    AnnualBudgetReportSerializer)


class ReportsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = AnnualBudgetReport.objects.all()
    serializer_class = AnnualBudgetReportSerializer
