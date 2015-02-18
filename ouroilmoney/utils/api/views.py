from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import (
    api_view, permission_classes
)
from ouroilmoney.utils.models import SmsMessage
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)

from  ouroilmoney.utils.api.serializers import SmsMessageSerializer
from rest_framework import viewsets
from rest_framework.decorators import list_route


class SmsMessageViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = SmsMessageSerializer
    queryset = SmsMessage.objects.filter(is_published=True)


    @list_route(methods=["get"])
    def sms(self, request):
        """
        Receive sms from smsgh
        """
        try:
           user = request.REQUEST.get('from')
           message = request.REQUEST.get('text')

           sms = SmsMessage.objects.create(user=user, message=message)
           sms.save()

           return Response(
               'Your message is noted. Thank you.', status=HTTP_200_OK)
        except Exception:
           return Response('Could not send message', status=HTTP_400_BAD_REQUEST)


    @list_route(methods=["get"])
    def verified(self,request):
        """
        Receive only verified and unverified sms
        """
        verifiedSms = SmsMessage.objects.filter(status="verified").exclude(is_published=False)
        serializer = SmsMessageSerializer(verifiedSms,many=True)
        return Response(serializer.data)
