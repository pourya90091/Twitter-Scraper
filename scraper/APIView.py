from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse
from utils.utils import send_email
from utils.enigma.enigma_code_decode import code as encode, rotors_config as true_rotors_config
from django.conf import settings


class LoginView(APIView):
    def post(self, req):
        try:
            rotors_config = (int(req.POST['r1']), int(req.POST['r2']), int(req.POST['r3']))
            plain = req.POST['plain']

            code = encode(plain.lower(), rotors_config)
            true_code = encode(settings.SECRET, true_rotors_config)

            if code != true_code:
                raise Exception('Access denied.')

            resp = {
                'url': reverse('twitter-index'),
                'code': code
            }

            return Response(resp, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_403_FORBIDDEN)


class EmailView(APIView):
    def post(self, req):
        try:
            email = req.POST['email']

            if email not in settings.WHITELIST:
                raise Exception('Access denied.')

            send_email(settings.EMAIL, email, settings.PASSWORD, 'True Rotors Config', str(true_rotors_config))

            resp = {
                'resp': 'Email sent.'
            }

            return Response(resp, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_403_FORBIDDEN)
