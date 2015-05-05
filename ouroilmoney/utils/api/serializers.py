from rest_framework import serializers
from ouroilmoney.utils.models import SmsMessage, Ministry, Partner, Field
from ouroilmoney.apps.liftings.api.serializers import LiftingSerializer


class SmsMessageSerializer(serializers.ModelSerializer):

    status = serializers.Field(source='get_status')
    user = serializers.Field(source='get_user')

    class Meta:
        model = SmsMessage
        fields = ('id', 'message', 'user', 'status', 'created')


class MinistrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Ministry
        fields = ('ministry',)


class OilPartnerSerializer(serializers.ModelSerializer):
    liftings = LiftingSerializer(many=True)

    class Meta:
        model = Partner
        fields = ('partner', 'liftings')


class OilFieldSerializer(serializers.ModelSerializer):
    liftings = LiftingSerializer(many=True)

    class Meta:
        model = Field
        fields = ('field', 'id', 'liftings')
