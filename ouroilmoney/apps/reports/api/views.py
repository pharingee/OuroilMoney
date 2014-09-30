from rest_framework import viewsets
from ouroilmoney.apps.reports.models import Report
from ouroilmoney.apps.reports.api.serializers import ReportSerializer


class ReportsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
