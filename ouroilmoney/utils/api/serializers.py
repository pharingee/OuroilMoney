from rest_framework import serializers
from ouroilmoney.utils.models import SmsMessage, Ministry, Partner, Field
from ouroilmoney.apps.projects.api.serializers import AnnualBudgetProjectSerializer



class SmsMessageSerializer(serializers.ModelSerializer):

    status = serializers.Field(source='get_status')
    user = serializers.Field(source='get_user')

    class Meta:
        model = SmsMessage
        fields = ('id', 'message', 'user', 'status', 'created')


class MinistrySerializer(serializers.ModelSerializer):
    annualbudgetprojects = AnnualBudgetProjectSerializer(many=True)

    class Meta:
        model = Ministry
        fields = ('ministry', 'annualbudgetprojects')


class OilPartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('partner',)


class OilFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = ('field',)
