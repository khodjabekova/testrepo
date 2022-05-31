from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics
from .models import About
from .serializers import AboutSerializer, AboutContactsSerializer, AboutSocialLinksSerializer
from rest_framework.response import Response


class AboutAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.get(pk=1)



class AboutContactAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]
    serializer_class = AboutContactsSerializer

    def get(self, request, format=None):
        queryset = About.objects.get(pk=1)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)



class AboutSocialLinksAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]
    serializer_class = AboutSocialLinksSerializer

    def get(self, request, format=None):
        queryset = About.objects.get(pk=1)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
