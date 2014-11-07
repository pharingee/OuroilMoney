from rest_framework import serializers
from ouroilmoney.apps.liftings.models import Lifting
from ouroilmoney.apps.reports.api.serializers import OtherReportSerializer


class LiftingSerializer(serializers.ModelSerializer):
    report = OtherReportSerializer()
    lifting_receipt_url = serializers.Field(source='get_lifting_receipt')

    class Meta:
        model = Lifting
        fields = (
            'report', 'date', 'volume_of_lifting',
            'selling_price', 'lifting_proceed','lifting_receipt_url')
