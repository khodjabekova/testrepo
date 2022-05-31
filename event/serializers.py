import base64
from django.core.files.images import get_image_dimensions
from rest_framework import serializers

from .models import Event, EventImages


class EventImagesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = EventImages
        fields = ['image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.image.file)
                img = open(obj.image.path, 'rb').read()
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


class EventDetailSerializer(serializers.ModelSerializer):
    images = EventImagesSerializer(many=True)

    class Meta:
        model = Event
        fields = ['slug', 'title', 'main_topic', 'content', 'images', 'start_time', 'end_time',
                  'responsible_org', 'address', 'pub_date', 'views', ]


class EventListSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Event
        fields = ["slug", 'title', 'main_topic', 'content', 'start_time', 'end_time',
                  'responsible_org', 'address', 'type', "pub_date", ]
