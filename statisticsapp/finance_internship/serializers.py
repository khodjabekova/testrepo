from rest_framework import serializers
from statisticsapp.models import FinanceInternshipStatistics, FinanceInternshipYear
from django.utils.translation import get_language

class FinanceInternshipAllYearsSerializer(serializers.ModelSerializer):
    field = serializers.SerializerMethodField()

    class Meta:
        model = FinanceInternshipStatistics
        fields = ['field', 'amount', ]

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


class FinanceInternshipStatisticsSerializer(serializers.ModelSerializer):
    field = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = FinanceInternshipStatistics
        fields = ['field', 'amount', ]


class FinanceInternshipYearSerializer(serializers.ModelSerializer):
    statistics = FinanceInternshipStatisticsSerializer(
        many=True, read_only=True)

    class Meta:
        model = FinanceInternshipYear
        fields = ('year', 'statistics')
