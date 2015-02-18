from rest_framework import serializers
from ouroilmoney.utils.models import SmsMessage


class SmsMessageSerializer(serializers.ModelSerializer):

    status = serializers.Field(source='get_status')
    user = serializers.Field(source='get_user')

    class Meta:
        model = SmsMessage
        fields = ('id', 'message', 'user', 'status', 'created')
