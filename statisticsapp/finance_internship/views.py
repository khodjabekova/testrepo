from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from statisticsapp.finance_internship.serializers import FinanceInternshipAllYearsSerializer, FinanceInternshipStatisticsSerializer, FinanceInternshipYearSerializer
from django.db.models import Sum

from statisticsapp.models import FinanceInternshipStatistics, FinanceInternshipYear


class FinanceInternshipByYearView(generics.RetrieveAPIView):
    """
    Ilmiy stajirovkalarni moliyalashtirish yillar bo'yicha
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = FinanceInternshipYearSerializer

    def get_object(self):
        year = self.kwargs['year']
        return FinanceInternshipYear.objects.prefetch_related('statistics').filter(year=year).first()


class FinanceInternshipYearsView(APIView):
    """
    Ilmiy stajirovkalarni moliyalashtirish yillar ro‘yhati
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        years = FinanceInternshipYear.objects.values_list('year', flat=True)
        return Response(years)


class FinanceInternshipAllYearsView(APIView):
    """
    Ilmiy stajirovkalarni moliyalashtirish yillar bo'yicha
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        statistics = FinanceInternshipStatistics.objects.select_related('field').values(
            'field__name_uz', 'field__name_uzb', 'field__name_ru', 'field__name_en').annotate(amount=Sum('amount'))
        serialized_data = FinanceInternshipAllYearsSerializer(
            statistics, many=True)
        return Response(serialized_data.data)
