import base64
from django.core.files.images import get_image_dimensions
from rest_framework import serializers

from menu.models import Menu
from .models import Post, PostAttachments, PostImages


class PostImagesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = PostImages
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


class PostMenuSerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Menu
        fields = ['parent', 'slug']


class PostListSerializer(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField()
    menu = PostMenuSerializer()

    class Meta:
        model = Post
        fields = ['slug', 'title', 'cover', 
                  'views', 'menu', 'pub_date']

    def get_cover(self, obj):
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


class PostAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachments
        fields = ['name', 'file', ]


class PostDetailSerializer(serializers.ModelSerializer):
    images = PostImagesSerializer(many=True)  # slugfield
    attachments = PostAttachmentsSerializer(many=True)
    class Meta:
        model = Post
        fields = ['images', 'title', 'content', 'views',
                  'pub_date', 'on_slider', 'attachments']
