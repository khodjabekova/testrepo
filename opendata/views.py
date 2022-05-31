from rest_framework import generics
from config.paginations import CustomPagination
from rest_framework.permissions import AllowAny
from django.db.models import Count

from opendata import serializers
from opendata.models import Opendata

class OpendataListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    queryset = Opendata.objects.annotate(files_count = Count('attachments')).filter(is_active=True)
    serializer_class = serializers.OpendataListSerializer

class OpendataByMenuListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    serializer_class = serializers.OpendataListSerializer

    def get_queryset(self):
        menu = self.kwargs['menu']
        queryset = Opendata.objects.annotate(files_count = Count('attachments')).filter(is_active=True, menu__slug=menu)
        return queryset

class OpendataDetailView(generics.RetrieveAPIView):
    queryset = Opendata.objects.annotate(files_count = Count('attachments')).filter(is_active=True)
    serializer_class = serializers.OpendataDetailSerializer
    lookup_field = 'slug'
