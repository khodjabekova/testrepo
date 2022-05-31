from rest_framework import generics
from config.paginations import CustomPagination
from rest_framework.permissions import AllowAny

from internship.models import Intern
from internship.serializers import InternListSerializer, InternDetailSerializer
from django_filters import FilterSet
from django_filters.rest_framework import CharFilter, DjangoFilterBackend

class InternFilterSet(FilterSet):
    name = CharFilter(field_name='name', method='filter_name')
    position = CharFilter(field_name='position', method='filter_position')
    place = CharFilter(field_name='place', method='filter_place')

    def filter_name(self, queryset, name, value):
        q = queryset.filter(
            name__icontains=value.lower())
        return q
    
    def filter_position(self, queryset, name, value):
        q = queryset.filter(
            position__icontains=value.lower())
        return q
    
    def filter_place(self, queryset, name, value):
        q = queryset.filter(
            place__icontains=value.lower())
        return q
    class Meta:
        model = Intern
        fields = ['name', 'position', 'place', 'start_date', 'end_date']

class InternListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    queryset = Intern.objects.all()
    serializer_class = InternListSerializer
    filterset_class = InternFilterSet


class InternDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Intern.objects.all()
    serializer_class = InternDetailSerializer
    lookup_field = 'slug'
