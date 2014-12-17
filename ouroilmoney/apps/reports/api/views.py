from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from ouroilmoney.apps.reports.models import (
    AnnualBudgetReport,
    CalendarOfReport,
    ConfirmReport)
from ouroilmoney.apps.reports.api.serializers import (
    AnnualBudgetReportSerializer, OtherReportSerializer, CalendarSerializer,
    ReportSerializer)


class AnnualBudgetReportViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Annual Budget Report Resource
    """
    queryset = AnnualBudgetReport.objects.exclude(is_published=False)
    serializer_class = AnnualBudgetReportSerializer

    @list_route(methods=["get"])
    def titles(self, request):
        """
        Get a list of Annual Budget Report Titles
        """
        title = AnnualBudgetReport.objects.values_list(
            'title', flat=True).order_by('title').distinct('title')
        return Response(title)


class OtherReportViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Other Reports  Resource
    """

    queryset = ConfirmReport.objects.exclude(is_published=False)
    serializer_class = OtherReportSerializer

    @list_route(methods=["get"])
    def first_quater_reports(self, request):
        """
        Get a list of first quarter reports
        """
        reports = ConfirmReport.objects.filter(
            report_type='1ST QUARTER REPORT')

        serializer = OtherReportSerializer(reports, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def second_quarter_reports(self, request):
        """
        Get a list of second quarter reports
        """
        reports = ConfirmReport.objects.all().filter(
            report_type='2ND QUARTER REPORT')
        serializer = OtherReportSerializer(reports, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def third_quarter_reports(self, request):
        """
        Get a list a third quarter reports
        """
        reports = ConfirmReport.objects.all().filter(
            report_type='3RD QUARTER REPORT')
        serializer = OtherReportSerializer(reports, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def fourth_quarter_reports(self, reqeust):
        """
        Get a list of fourth quarter reports
        """
        reports = ConfirmReport.objects.all().filter(
            report_type='4TH QUARTER REPORT')
        serializer = OtherReportSerializer(reports, many=True)
        return Response(serializer.data)

    @list_route(methods=["get"])
    def monitoring_reports(self, reqeust):
        """
        Get a list of monitoring reports.
        Monitoring reports refers to reports that are suppose
        to confirm if reports coming in are really correct.
        """
        reports = ConfirmReport.objects.all().filter(
            report_type='MONITORING REPORT')
        serializer = OtherReportSerializer(reports, many=True)
        return Response(serializer.data)


class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    """
    All Report Resource
    """
    queryset = AnnualBudgetReport.objects.exclude(is_published=False)
    serializer_class = ReportSerializer

    @list_route(methods=["get"])
    def calendar(self, reqeust):
        """
        Get calendar of incoming reports
        """
        calendar = CalendarOfReport.objects.exclude(is_published=False)
        serializer = CalendarSerializer(calendar, many=True)
        return Response(serializer.data)

