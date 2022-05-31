from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['fullname', 'phone', 'region', 'address',
                  'file', 'mail', 'message']
