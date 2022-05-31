from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                serializer.data['fullname'],
                serializer.data['message'],
                settings.EMAIL_HOST_USER, #murojaat@innofund.uz
                [serializer.data['mail']],
                fail_silently=False,
            )
            return Response({
                'status': 201,
                'message': 'Message sended!',
            })
        else:
            return Response({
                'status': 400,
                'message': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)


class SendErrorMessageView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]


    def post(self, request, *args, **kwargs):

        try:
            send_mail(
                "Saytda xatolik topildi",
                request.data['message'],
                settings.EMAIL_HOST_USER, #murojaat@innofund.uz from
                [settings.EMAIL_HOST_USER], # to xatolik@innofund.uz
                fail_silently=False,
            )
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)