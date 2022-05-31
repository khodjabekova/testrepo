import base64

from django.core.files.images import get_image_dimensions
from django.utils.translation import get_language, activate
from rest_framework import serializers

from config.regions import RegionsEnum

from .models import AppealQuarterDetailStatistics, AppealQuarterStatistics, AppealStatistics, Country, CountryStatistics, EquipmentPurchaseStatistics, Region, RegionStatistics, ScienceField, FinanceEntity, InternCount, \
    RegionSight, RegionSightImages, ScientificInternship, ScientificInternshipStatistic, AnnualCost, \
    YoungScientistInternship, NormativeDocument
from django.db.models import Sum


class ScienceFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScienceField
        fields = ('name', 'icon')


class CountryStatisticsSerializer(serializers.ModelSerializer):
    science_field = ScienceFieldSerializer()

    class Meta:
        model = CountryStatistics
        fields = ('science_field', 'count')


class CountryListSerializer(serializers.ModelSerializer):
    # statistics = CountryStatisticsSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['name', 'code']


class CountryDetailsSerializer(CountryListSerializer):
    count = serializers.IntegerField()
    statistics = CountryStatisticsSerializer(many=True, read_only=True)

    class Meta(CountryListSerializer.Meta):
        model = Country
        fields = CountryListSerializer.Meta.fields + ['count', 'statistics']


class RegionStatisticsSerializer(serializers.ModelSerializer):
    science_field = ScienceFieldSerializer()

    class Meta:
        model = RegionStatistics
        fields = ('science_field', 'count')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']


class RegionStatisticsListSerializer(serializers.ModelSerializer):
    statistics = serializers.SerializerMethodField()
    total = serializers.IntegerField()

    class Meta:
        model = RegionStatistics
        fields = ['statistics', 'total']

    def get_statistics(self, obj):
        items = RegionStatistics.objects.all()
        statistics = items.values(
            'science_field__name').annotate(count=Sum('count'))
        return statistics


class RegionDetailsSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()
    statistics = RegionStatisticsSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ['name', 'count', 'statistics']


class FinanceEntityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceEntity
        fields = ['year', 'sum']


class InternCountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternCount
        fields = ['year', 'count']


class RegionSightListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')
    region = serializers.SerializerMethodField('get_region')

    class Meta:
        model = RegionSight
        fields = ['slug', 'title', 'content', 'region', 'image']

    def get_region(self, obj):
        lang = get_language()
        if lang == 'uz':
            type_lang = RegionsEnum[obj.region].value[0]
        elif lang == 'ru':
            type_lang = RegionsEnum[obj.region].value[0]
        elif lang == 'uzb':
            type_lang = RegionsEnum[obj.region].value[0]
        elif lang == 'en':
            type_lang = RegionsEnum[obj.region].value[0]
        else:
            type_lang = obj.region
        return type_lang

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.image.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                base_to_str = data_base64.decode('utf-8')
                data = {
                    'src': path,
                    'weight': w,
                    'height': h,
                    "base64": "data:image/jpg;base64" + base_to_str
                }
                return data
            except Exception:
                return None
        else:
            return None


class RegionSightImagesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = RegionSightImages
        fields = ['image', ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.image.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_string = data_base64.decode('utf-8')
                data = {
                    "src": path,
                    'weight': w,
                    "height": h,
                    "base64": "data:image/jpg;base64," + byte_to_string,
                }
                return data
            except Exception:
                return None
        else:
            return None


class RegionSightDetailSerializer(RegionSightListSerializer):
    images = RegionSightImagesSerializer(many=True, read_only=True)

    class Meta(RegionSightListSerializer.Meta):
        model = RegionSight
        fields = ['slug', 'title', 'content', 'region', 'images']


class ScientificInternshipStatisticSerializer(serializers.ModelSerializer):
    field = serializers.SerializerMethodField()
    class Meta:
        model = ScientificInternshipStatistic
        fields = ['field', 'amount']

    def get_field(self, obj):
        lang = get_language()
        if lang == 'en':
            return obj['field__name_en']
        elif lang == 'uzb':
            return obj['field__name_uzb']
        elif lang == 'ru':
            return obj['field__name_ru']
        else:
            return obj['field__name_uz']


class ScientificInternshipAllSerializer(serializers.ModelSerializer):
    statistics = serializers.SerializerMethodField()

    class Meta:
        model = ScientificInternship
        fields = ['statistics', ]

    def get_statistics(self, obj):
        
        items = ScientificInternshipStatistic.objects.all()
        statistics = items.values('field__name_uz', 'field__name_uzb','field__name_ru','field__name_en').annotate(amount=Sum('amount'))
        result = ScientificInternshipStatisticSerializer(
            statistics, many=True).data
        return result


class ScientificInternshipByYearsSerializer(serializers.ModelSerializer):
    statistics = serializers.SerializerMethodField()

    class Meta:
        model = ScientificInternship
        fields = ['year', 'statistics', ]

    def get_statistics(self, obj):
        
        items = ScientificInternshipStatistic.objects.filter(scientific_internship__year=obj['year'])
        statistics = items.values('field__name_uz', 'field__name_uzb','field__name_ru','field__name_en', 'field__index').annotate(amount=Sum('amount')).order_by('field__index')
        result = ScientificInternshipStatisticSerializer(
            statistics, many=True).data
        return result


class ScientificInternshipSerializer(serializers.ModelSerializer):
    statistics = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = ScientificInternship
        fields = ['year', 'successful', 'rejected', 'statistics', 'total']

    def get_statistics(self, obj):
        items = ScientificInternshipStatistic.objects.filter(scientific_internship__region=obj['region'],
                                                             scientific_internship__year=obj['year'])
        statistics = items.values('field__name_uz', 'field__name_uzb','field__name_ru','field__name_en').annotate(amount=Sum('amount'))
        result = ScientificInternshipStatisticSerializer(
            statistics, many=True).data
        return result

    def get_total(self, obj):
        items = ScientificInternshipStatistic.objects.filter(scientific_internship__region=obj['region'],
                                                             scientific_internship__year=obj['year'])
        total = items.values('scientific_internship__region').annotate(
            total=Sum('amount'))[0]['total']
        return total


class ScientificInternshipDetailByRegionSerializer(serializers.ModelSerializer):
    statistics = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = ScientificInternship
        fields = ['region', 'successful', 'rejected', 'statistics', 'total']

    def get_statistics(self, obj):
        request = self.context['request']
        lang = get_language()
        activate(lang)
        items = ScientificInternshipStatistic.objects.filter(
            scientific_internship__region=obj['region'])
        statistics = items.values('field__name_uz', 'field__name_uzb','field__name_ru','field__name_en', 'field__index').annotate(amount=Sum('amount')).order_by('field__index')
        result = ScientificInternshipStatisticSerializer(
            statistics, many=True, context={'lang': lang}).data
        return result

    def get_total(self, obj):
        items = ScientificInternshipStatistic.objects.filter(
            scientific_internship__region=obj['region'])
        total = items.values('scientific_internship__region').annotate(
            total=Sum('amount'))[0]['total']
        return total


class ScientificInternshipDetailByRegionYearsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScientificInternship
        fields = ['year']


class AnnualCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualCost
        fields = ['year', 'fields', 'cost']


class YoungScientistInternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoungScientistInternship
        fields = ['scientist', 'country', 'field', 'relation']


class AppealStatisticsByApplicantSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = AppealStatistics
        fields = ['individual', 'legal', 'total']

    def get_total(self, obj):
        return obj.individual + obj.legal


class AppealStatisticsByStatusSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = AppealStatistics

        fields = ['closed', 'repeated', 'total']

    def get_total(self, obj):
        return obj.closed + obj.repeated


class AppealQuarterDetailStatisticsSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = AppealQuarterDetailStatistics
        fields = ['appeal_type', 'in_progress',
                  'redirected', 'closed', 'total']

    def get_total(self, obj):
        try:
            result = obj.closed + obj.in_progress + obj.redirected
        except:
            result = obj['closed'] + obj['in_progress'] + obj['redirected']

        return result


class AppealQuarterStatisticsSerializer(serializers.ModelSerializer):
    all = serializers.SerializerMethodField()
    statistics = AppealQuarterDetailStatisticsSerializer(
        many=True, read_only=True)

    class Meta:
        model = AppealQuarterStatistics

        fields = ['year', 'quarter', 'statistics', 'all']

    def get_all(self, obj):
        statistics = obj.statistics.all()
        in_progress = sum(statistics.values_list('in_progress', flat=True))
        redirected = sum(statistics.values_list('redirected', flat=True))
        closed = sum(statistics.values_list('closed', flat=True))
        # total = in_progress + redirected + closed
        result = AppealQuarterDetailStatisticsSerializer({'appeal_type': 'all', 'in_progress': in_progress,
                                                          'redirected': redirected, 'closed': closed}).data
        return result


class EquipmentPurchaseStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentPurchaseStatistics
        fields = ['title', 'equipment_count', 'invested']
