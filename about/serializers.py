import base64
from django.core.files.images import get_image_dimensions
from rest_framework import serializers
from .models import About, AboutImages


class AboutImagesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')
    
    class Meta:
        model = AboutImages
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

class AboutSerializer(serializers.ModelSerializer):
    images = AboutImagesSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = ['description',  'images' ]



class AboutContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ['phone', 'email', 'address', 'transport', 'ltd', 'lng',
                  'facebook_url', 'instagram_url', 'telegram_url', 'youtube_url']




class AboutSocialLinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ['facebook_url', 'instagram_url',
                  'telegram_url', 'youtube_url']
