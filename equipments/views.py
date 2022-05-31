from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from config.paginations import CustomPagination
from .models import Equipment, Type
from .serializers import EquipmentDetailSerializer, EquipmentListSerializer, EquipmentTypeListSerializer
from django.utils.translation import get_language
from django_filters.rest_framework import CharFilter, DjangoFilterBackend
from django_filters import FilterSet
from config.regions import RegionsEnum


class EquipmentRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Equipment.objects.all()
    serializer_class = EquipmentDetailSerializer
    lookup_field = 'slug'

    def get_object(self):
        obj = super().get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=['views', ])
        return obj


class EquipmentFilter(FilterSet):
    name = CharFilter(
        field_name='name', method='filter_name')

    def filter_name(self, queryset, name, value):
        q = queryset.filter(
            name__icontains=value.lower())
        return q

    type = CharFilter(
        field_name='type', method='filter_type')

    def filter_type(self, queryset, name, value):
        q = queryset.filter(
            type__slug=value)
        return q

    class Meta:
        model = Equipment
        fields = ['name', 'region', 'pub_date', 'type', 'on_slider']


class EquipmentListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    queryset = Equipment.objects.filter(is_active=True)
    serializer_class = EquipmentListSerializer
    filter_backends = (DjangoFilterBackend,
                       filters.OrderingFilter)
    filterset_class = EquipmentFilter
    ordering_fields = ('pub_date', 'views')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class EquipmentOnSliderListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    queryset = Equipment.objects.filter(is_active=True, on_slider=True)
    serializer_class = EquipmentDetailSerializer


class EquipmentTypeListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Type.objects.filter(is_active=True)
    serializer_class = EquipmentTypeListSerializer


class RegionList(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        lang = get_language()
        if lang == 'en':
            i = 3
        elif lang == 'uzb':
            i = 1
        elif lang == 'ru':
            i = 2
        else:
            i = 0

        region_list = [{r.name: r.value[i]} for r in RegionsEnum]
        return Response(region_list)
