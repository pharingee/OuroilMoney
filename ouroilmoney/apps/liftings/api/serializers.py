from rest_framework import serializers
from ouroilmoney.utils.api.serializers import OilPartnerSerializer, OilFieldSerializer
from ouroilmoney.apps.liftings.models import Lifting
from ouroilmoney.apps.reports.api.serializers import OtherReportSerializer


class LiftingSerializer(serializers.ModelSerializer):
    partner = OilPartnerSerializer()
    report = OtherReportSerializer()
    field = OilFieldSerializer()
    lifting_receipt_url = serializers.Field(source='get_lifting_receipt')

    class Meta:
        model = Lifting
        fields = (
            'report',
            'date',
            'volume_of_lifting',
            'selling_price',
            'lifting_proceed',
            'partner',
            'field',
            'lifting_receipt_url')
