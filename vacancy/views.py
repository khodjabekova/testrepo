
from rest_framework import generics
from rest_framework.permissions import AllowAny
from config.paginations import CustomPagination

from vacancy.models import Vacancy
from vacancy.serilaizers import VacancyListSerializer


class VacancyListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    serializer_class = VacancyListSerializer

    def get_queryset(self):
        return Vacancy.objects.exclude(title__isnull=True)
