from rest_framework import serializers
from ouroilmoney.utils.models import SmsMessage


class SmsMessageSerializer(serializers.ModelSerializer):

    get_status = serializers.Field(source='get_status')

    class Meta:
        model = SmsMessage
        fields = ('id', 'message', 'user', 'get_status', 'created')
