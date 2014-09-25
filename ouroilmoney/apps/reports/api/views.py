from rest_framework import viewsets
from ouroilmoney.apps.reports.models import Reports
from ouroilmoney.apps.reports.api.serializers import ReportsSerializer


class ReportsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing accounts.
    """
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
