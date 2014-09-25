from rest_framework import serializers
from ouroilmoney.apps.reports.models import Reports


class  ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reports