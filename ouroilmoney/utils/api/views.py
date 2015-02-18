from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import (
    api_view, permission_classes
)


@api_view(['GET'])
@permission_classes((AllowAny,))
def sms(request):
    try:
        user = request.REQUEST.get('from')
        message = request.REQUEST.get('text')

        sms = SMSMessage.objects.create(user=user, message=message)
        sms.save()

        return Response(
            'Your message is noted. Thank you.', status=HTTP_200_OK)
    except Exception, err:
        return Response('Could not send message', status=HTTP_400_BAD_REQUEST)
