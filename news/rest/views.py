from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.mail import send_mail
from smtplib import SMTPException


@api_view(['GET', 'POST'])
def idfund_form_commit(request):
    if request.method == 'POST':
        # print(request.data['project_requirments'])
        message = request.data['idfund_invest_demand']
        try:
            send_mail(
                'Subject here',
                message,
                'web@gsjkjt.com',
                ['gelinlandev@qq.com'],
                fail_silently=False,
                )
        except SMTPException as e:
            print(e)
        return Response("okay", status=status.HTTP_400_BAD_REQUEST)
    return Response("okay", status=status.HTTP_400_BAD_REQUEST)