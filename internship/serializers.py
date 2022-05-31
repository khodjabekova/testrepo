import base64
from django.core.files.images import get_image_dimensions
from rest_framework import serializers
from internship.models import Intern, InternPhoto


class InternListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo')

    class Meta:
        model = Intern
        fields = ['slug', 'name', 'position', 'place', 'photo']

    def get_photo(self, obj):
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


class InternshipPhotosSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo')

    class Meta:
        model = InternPhoto
        fields = ['name', 'photo']

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.photo:
            image_url = obj.photo.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.photo.file)
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


class InternDetailSerializer(InternListSerializer):
    # photos = InternshipPhotosSerializer(many=True, read_only=True)
    photos = serializers.SerializerMethodField('get_photos')


    class Meta(InternListSerializer.Meta):
        model = Intern
        fields = InternListSerializer.Meta.fields + \
            ['phone', 'email', 'biography', 'start_date', 'end_date', 'photos']


    def get_photos(self, obj):
        request = self.context['request']
        data = obj.photos.all()
        return InternshipPhotosSerializer(data, many=True, context = {'request': request}).data