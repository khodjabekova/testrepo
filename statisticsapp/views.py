from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import get_language

from gallery.models import VideoGallery, PhotoGalleryImages
from post.models import Post
from . import serializers
from .models import AppealQuarterStatistics, AppealStatistics, Country, EquipmentPurchaseStatistics, Region, \
    FinanceEntity, InternCount, RegionSight, ScienceField, ScientificInternship, AnnualCost, ScientificInternshipStatistic, \
    YoungScientistInternship, CountryStatistics, RegionStatistics, NormativeDocument
from .country import CountryEnum
from config.regions import RegionsEnum
from .serializers import ScientificInternshipAllSerializer, ScientificInternshipByYearsSerializer, ScientificInternshipSerializer, ScientificInternshipStatisticSerializer
from .types import FinanceEntityType
from django.db.models import Sum, Count, F


class ScienceFieldListView(ListAPIView):
    """
    Barcha yo‘nalishlar ro‘yhati
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = ScienceField.objects.all()
    serializer_class = serializers.ScienceFieldSerializer


class CountryListView(ListAPIView):
    """
    Barcha mamlakatlar ro'yhati
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Country.objects.all()
    serializer_class = serializers.CountryListSerializer


class RegionStatListView(APIView):
    """
    Statistikasi mavjud bo'lgan hududlar ro‘yhati
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        queryset = RegionStatistics.objects.values(
            'region__name').values_list('region__name', flat=True).distinct()
        return Response(queryset)


class CountryDetailView(RetrieveAPIView):
    """
    Mamlatning statistikasi
    mamlakat code - bo‘yicha olinadi
    barcha mamlakatlar codini /statistics/ dan olsa bo‘ladi
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Country.objects.annotate(count=Sum('statistics__count')).all()
    serializer_class = serializers.CountryDetailsSerializer
    lookup_field = 'code'


class RegionDetailView(RetrieveAPIView):
    """
    Berilgan hudud bo‘yicha yo‘nalishlar kesmida statistika
    Barcha hududlar ro‘yhatini statistics/regions dan olsa bo‘ladi
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Region.objects.annotate(count=Sum('statistics__count')).all()
    serializer_class = serializers.RegionDetailsSerializer
    lookup_field = 'name'


class FinanceDetail(RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = FinanceEntity.objects.all()
    serializer_class = serializers.FinanceEntityListSerializer
    lookup_field = 'year'


class CountryList(APIView):
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

        country_list = [{r.name: r.value[i]} for r in CountryEnum]
        return Response(country_list)


class RegionsList(APIView):
    """
    Barcha hududlar ro‘yhati
    """
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


class CountPostByYearView(APIView):
    """
    Kontent bo‘yicha statistika (yangiliklar yillar kesmida)
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        items = Post.objects.annotate(
            year=F('pub_date__year')).order_by('pub_date')
        count = items.values('year').annotate(
            total=Count('id')).order_by('year')
        return Response(count)


class CountPostByMonthView(APIView):
    """
    Kontent bo‘yicha statistika (yangiliklar oylar kesmida)
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        items = Post.objects.annotate(year=F('pub_date__year'),
                                      month=F('pub_date__month')).order_by('pub_date')
        count = items.values('year', 'month').annotate(
            total=Count('id')).order_by('year', 'month')
        return Response(count)


class CountPostByDayView(APIView):
    """
    Kontent bo‘yicha statistika (yangiliklar kunlar kesmida)
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        items = Post.objects.annotate(day=F('pub_date')).order_by('pub_date')
        count = items.values('day').annotate(
            total=Count('id')).order_by('pub_date')
        return Response(count)


class FinanceEntityList(APIView):
    """
    Innovatsion faoliyat subyektlarini moliyalashtirish statistika turlari 
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        lang = get_language()
        if lang == "en":
            i = 3
        elif lang == "uzb":
            i = 1
        elif lang == 'ru':
            i = 2
        else:
            i = 0
        finance_list = [{r.name: r.value[i]} for r in FinanceEntityType]
        return Response(finance_list)


class FinanceEntityByType(ListAPIView):
    """
    Innovatsion faoliyat subyektlarini moliyalashtirish statistikasi
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.FinanceEntityListSerializer

    def get_queryset(self):
        type = self.kwargs['type']
        queryset = FinanceEntity.objects.filter(
            type=type).exclude(is_active=False).order_by('-year')
        return queryset


class InternCountListView(ListAPIView):
    """
    Amaliyotchilar soni
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = InternCount.objects.all()
    serializer_class = serializers.InternCountListSerializer


class RegionSightHasListView(APIView):
    """
    Mintaqaning diqqatga sazovor joylari bo‘lgan hududlar ro‘yhati
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        items = RegionSight.objects.all().exclude(is_active=False)
        queryset = items.values('region').values_list(
            'region', flat=True).distinct()
        return Response(queryset)


class RegionSightListView(ListAPIView):
    """
    Berilgan hudud bo‘yicha shu hududdagi mintaqaning diqqatga sazovor joylari ro‘yhati
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.RegionSightListSerializer

    def get_queryset(self):
        region = self.kwargs['region']
        queryset = RegionSight.objects.filter(
            region=region).exclude(is_active=False)
        return queryset


class RegionSightDetailView(RetrieveAPIView):
    """
    Berilgan hudud va slug bo‘yicha mintaqaning diqqatga sazovor joy
    Detail page
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = RegionSight.objects.all()
    serializer_class = serializers.RegionSightDetailSerializer
    lookup_field = 'slug'


class CountFotoAndVideoView(APIView):
    """
    Kontent bo'yicha statistika (foto, video va umumiy statistika)
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        videos = len(VideoGallery.objects.all())
        photos = len(PhotoGalleryImages.objects.all())
        return Response({"photos": photos, "videos": videos, 'total': videos + photos})


class ScientificInternshipView(APIView):
    """
    Barcha ilmiy stajirovkalar muvaffaqiyatli yoki rad etilganlar ro‘yhati yillar kesmida
    type - successful or rejected
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, type, format=None):
        items = ScientificInternship.objects.all()

        if type == 'successful':
            queryset = items.values('year').annotate(
                count=Sum('successful')).values('year', 'count').order_by('-year')
        elif type == 'rejected':
            queryset = items.values('year').annotate(
                count=Sum('rejected')).values('year', 'count').order_by('-year')
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        # successful = sum(items.values_list('successful', flat=True))
        # rejected = sum(items.values_list('rejected', flat=True))
        # return Response({'successful': successful, 'rejected': rejected})
        return Response(queryset)


class ScientificInternshipAllView(ListAPIView):
    """
    Ilmiy stajirovkalar statistikasi
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = ScientificInternshipStatisticSerializer

    def get_queryset(self):
        items = ScientificInternshipStatistic.objects.all()
        statistics = items.values('field__name_uz', 'field__name_uzb','field__name_ru','field__name_en', 'field__index').annotate(amount=Sum('amount')).order_by('field__index')
        return statistics

class ScientificInternshipYearsView(APIView):
    """
    Ilmiy stajirovkalar statistikasi mavjud bo‘lgan yillar ro‘yhati
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        queryset = ScientificInternship.objects.values_list(
            'year', flat=True).distinct().order_by('-year')
        return Response(queryset)


class ScientificInternshipByYearView(ListAPIView):
    """
    Ilmiy stajirovkalar statistikasi yillar bo‘yicha
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = ScientificInternshipByYearsSerializer

    def get_queryset(self):
        year = self.kwargs['year']
        items = ScientificInternship.objects.filter(
            year=year).exclude(is_active=False)
        queryset = items.values('year').distinct()
        return queryset





class ScientificInternshipRegionListView(APIView):

    """
    Ilmiy stajirovkalar statistikasi mavjud bo‘lgan hududlar ro‘yhati
    """
    
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        queryset = ScientificInternship.objects.values(
            'region').values_list('region', flat=True).distinct()
        return Response(queryset)


class ScientificInternshipDetailByRegionView(ListAPIView):
    """
    Ilmiy stajirovkalar statistikasi hududlar bro‘yicha
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.ScientificInternshipDetailByRegionSerializer

    def get_queryset(self):
        region = self.kwargs['region']
        items = ScientificInternship.objects.filter(region=region)
        queryset = items.values('region').annotate(successful=Sum('successful'),
                                                   rejected=Sum('rejected')
                                                   )
        return queryset


class ScientificInternshipByRegionYearsView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    # serializer_class = serializers.ScientificInternshipDetailByRegionYearsSerializer

    def get(self, request, region, format=None):
        queryset = ScientificInternship.objects.filter(
            region=region).values_list('year', flat=True).distinct().order_by('-year')
        return Response(queryset)


class ScientificInternshipDetailByRegionYearView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = ScientificInternshipSerializer

    def get_queryset(self):
        region = self.kwargs['region']
        year = self.kwargs['year']
        items = ScientificInternship.objects.filter(
            region=region, year=year).exclude(is_active=False)
        queryset = items.values('year', 'region').annotate(
            successful=Sum('successful'),
            rejected=Sum('rejected')
        )
        return queryset


class AnnualCostListView(ListAPIView):
    """
    Yillik xarajatlar (turlar bo'yicha)
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = AnnualCost.objects.all().order_by('year')
    serializer_class = serializers.AnnualCostSerializer


class YoungScientistInternshipListView(RetrieveAPIView):
    """
    Yosh olimlarni ilmiy stajirovkaga yuborish bo'yicha statistik ma'lumot
    Bosh sahifadagi statistika
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.YoungScientistInternshipSerializer

    def get_object(self):
        return YoungScientistInternship.objects.first()


class RegionStatisticsListView(ListAPIView):
    """
    Barcha hududlar bo‘yicha umumiy yo‘nalishlar kesmida statistika ro‘yhati
    (scientific fields statistics united by all region)
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.RegionStatisticsListSerializer

    def get_queryset(self):
        items = RegionStatistics.objects.values_list('count', flat=True)
        total = sum(items)
        return [{'total': total}]


class NormativeDocumentByDayView(APIView):
    """
    Me‘yoriy hujjatlar statisikasi (kunlar kesmida)
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        items = NormativeDocument.objects.annotate(
            day=F('date')).order_by('date')
        queryset = items.values('day').annotate(
            total=Sum('count')).order_by('date')
        return Response(queryset)


class NormativeDocumentMonthView(APIView):
    """
    Me‘yoriy hujjatlar statisikasi (oylar kesmida)
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        items = NormativeDocument.objects.annotate(
            year=F('date__year'), month=F('date__month')).order_by('date')
        queryset = items.values('year', 'month').annotate(
            total=Sum('count')).order_by('year', 'month')
        return Response(queryset)


class NormativeDocumentYearView(APIView):
    """
    Me‘yoriy hujjatlar statisikasi (yillar kesmida)
    """
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        items = NormativeDocument.objects.annotate(
            year=F('date__year')).order_by('date')
        queryset = items.values('year').annotate(
            total=Sum('count')).order_by('year')
        return Response(queryset)


class AppealStatisticsByApplicantView(RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.AppealStatisticsByApplicantSerializer

    def get_object(self):
        return AppealStatistics.objects.get(pk=1)


class AppealStatisticsByStatusView(RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.AppealStatisticsByStatusSerializer

    def get_object(self):
        return AppealStatistics.objects.get(pk=1)


class AppealQuarterStatisticsView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.AppealQuarterStatisticsSerializer
    queryset = AppealQuarterStatistics.objects.all()


class EquipmentPurchaseStatisticsView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.EquipmentPurchaseStatisticsSerializer
    queryset = EquipmentPurchaseStatistics.objects.all().order_by('index')
