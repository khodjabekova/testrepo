from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from config.paginations import CustomPagination

from useful_link import serializers
from useful_link.models import UsefulLink


class UsefulLinkListView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    # pagination_class = CustomPagination
    serializer_class = serializers.UsefulLinkListSerializer

    def get_queryset(self):
        queryset = UsefulLink.objects.exclude(title__isnull=True)
        return queryset


# class UsefulLinkDetailView(RetrieveAPIView):
#     authentication_classes = []
#     permission_classes = [AllowAny]
#     queryset = UsefulLink.objects.all()
#     serializer_class = serializers.UsefulLinkDetailSerializer
#     lookup_field = 'slug'
