from rest_framework import serializers
from .models import Menu
from rest_framework_recursive.fields import RecursiveField

class MenuSerializer(serializers.ModelSerializer):
    sub_menu = RecursiveField(many=True,source='active_sub_menu')

    class Meta:
        model = Menu
        fields = ['slug', 'title', 'type', 'link', 'index', 'sub_menu', 'note']
