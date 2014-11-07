from rest_framework import serializers
from ouroilmoney.apps.reports.models import AnnualBudgetReport
from ouroilmoney.apps.reports.models import ConfirmReport
from ouroilmoney.apps.revenues.api.serializers import (
    AnnualBudgetRevenueSerializer,)


class OtherReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmReport



class AnnualBudgetReportSerializer(serializers.ModelSerializer):
    report_type = serializers.SerializerMethodField('type')
    otherreports = OtherReportSerializer(many=True)
    document_url= serializers.Field(source='get_document')

    def type(self, obj):
        return 'Annual Budget Report'



    class Meta:
        model = AnnualBudgetReport
        fields = (
            'report_type', 'title', 'date','otherreports',
            'source_of_report', 'source_url','document_url')


class ReportSerializer(serializers.ModelSerializer):
    otherreports = OtherReportSerializer(many=True)
    revenues = AnnualBudgetRevenueSerializer(many=True)
    report_type = serializers.SerializerMethodField('type')
    document_url= serializers.Field(source='get_document')


    def type(self, obj):
        return 'Annual Budget Report'

    class Meta:
        model = AnnualBudgetReport
        fields = (
            'id', 'title', 'date', 'report_type',
            'source_of_report',
            'source_url','document_url', 'otherreports',
            'revenues', 'created', 'modified')
