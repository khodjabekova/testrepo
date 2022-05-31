import base64

from rest_framework import serializers
from django.core.files.images import get_image_dimensions
from rest_framework.serializers import ModelSerializer

from config import settings
from gallery.models import Gallery, PhotoGallery, PhotoGalleryImages, VideoGallery


class PhotoGalleryImagesSerializer(ModelSerializer):
    image = serializers.SerializerMethodField("get_image")

    class Meta:
        model = PhotoGalleryImages
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


class GallerySerializer(ModelSerializer):
    cover = serializers.SerializerMethodField('get_cover')

    class Meta:
        model = Gallery
        fields = ['slug', 'name', 'cover', ]

    def get_cover(self, obj):
        request = self.context.get('request')
        if obj.cover:
            cover_url = obj.cover.url
            path = request.build_absolute_uri(cover_url)
            try:
                w, h = get_image_dimensions(obj.cover.file)
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


class PhotoGallerySerializer(GallerySerializer):

    class Meta(GallerySerializer.Meta):
        model = PhotoGallery
        fields = GallerySerializer.Meta.fields


class PhotoGalleryDetailSerializer(GallerySerializer):
    images = serializers.SerializerMethodField()

    class Meta(GallerySerializer.Meta):
        model = PhotoGallery
        fields = GallerySerializer.Meta.fields + ['images']

    def get_images(self, obj):
        request = self.context.get('request')

        qs = PhotoGalleryImages.objects.filter(gallery=obj).exclude(image='')
        serializer = PhotoGalleryImagesSerializer(instance=qs, many=True,context={'request': request})
        return serializer.data


class VideoGallerySerializer(GallerySerializer):
    class Meta(GallerySerializer.Meta):
        model = VideoGallery
        fields = GallerySerializer.Meta.fields + ['link']
