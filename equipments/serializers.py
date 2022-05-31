import base64
from django.core.files.images import get_image_dimensions
from rest_framework import serializers
from .models import Equipment, EquipmentImages, Type
from django.utils.translation import get_language
from config.regions import RegionsEnum


class EquipmentImagesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = EquipmentImages
        fields = ['image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.image.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_str = data_base64.decode("utf-8")
                data = {
                    'src': path,
                    'width': w,
                    'height': h,
                    'base64': "data:image/jpg;base64," + byte_to_str,
                }
                return data
            except Exception:
                return None
        else:
            return None


class EquipmentDetailSerializer(serializers.ModelSerializer):
    images = EquipmentImagesSerializer(many=True)
    region = serializers.SerializerMethodField(method_name='get_region')

    class Meta:
        model = Equipment
        fields = ['slug', 'name', 'content', 'images', 'region',
                  'pub_date', 'views', 'type', ]

    def get_region(self, instance):
        lang = get_language()
        if 'uz' == lang:
            type_lang = RegionsEnum[instance.region].value[0]
        elif 'uzb' == lang:
            type_lang = RegionsEnum[instance.region].value[1]
        elif 'ru' == lang:
            type_lang = RegionsEnum[instance.region].value[2]
        elif 'en' == lang:
            type_lang = RegionsEnum[instance.region].value[3]
        else:
            type_lang = instance.region
        return type_lang


class EquipmentListSerializer(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField('get_thumbnail')
    region = serializers.SerializerMethodField(method_name='get_region')
    type = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Equipment
        fields = ['slug', 'name', 'cover',
                  'region', 'pub_date', 'views', 'type']

    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            image_url = obj.thumbnail.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.thumbnail.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_str = data_base64.decode("utf-8")
                data = {
                    'src': path,
                    'width': w,
                    'height': h,
                    'base64': "data:image/jpg;base64," + byte_to_str,
                }
                return data
            except Exception:
                return None
        else:
            return None

    def get_region(self, instance):
        lang = get_language()
        if instance.region:
            if 'uz' == lang:
                type_lang = RegionsEnum[instance.region].value[0]
            elif 'uzb' == lang:
                type_lang = RegionsEnum[instance.region].value[1]
            elif 'ru' == lang:
                type_lang = RegionsEnum[instance.region].value[2]
            elif 'en' == lang:
                type_lang = RegionsEnum[instance.region].value[3]
            else:
                type_lang = instance.region
            return type_lang
        else:
            return None


class EquipmentTypeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ['slug', 'name', ]
