from rest_framework.permissions import AllowAny
from rest_framework import generics
from config.paginations import CustomPagination

from gallery.models import PhotoGallery, VideoGallery
from gallery.serializers import PhotoGalleryDetailSerializer, PhotoGallerySerializer, VideoGallerySerializer
from django_filters.rest_framework import DjangoFilterBackend


class PhotoGalleryRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGalleryDetailSerializer
    lookup_field = 'slug'


class PhotoGalleryListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['on_slider', ]


class VideoGalleryRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
    lookup_field = 'slug'


class VideoGalleryListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['on_slider', ]
