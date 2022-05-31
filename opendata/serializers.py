from rest_framework.serializers import ModelSerializer, IntegerField


from opendata.models import Opendata, OpendataAttachments

class OpendataAttachmentsSerializer(ModelSerializer):
    class Meta:
        model = OpendataAttachments
        fields = ['name', 'file', ]


class OpendataListSerializer(ModelSerializer):
    files_count = IntegerField()
    attachments = OpendataAttachmentsSerializer(many=True, read_only=True)

    class Meta:
        model = Opendata
        fields = ['slug', 'title', 'link', 'ilova', 'files_count', 'attachments']




class OpendataDetailSerializer(ModelSerializer):
    attachments = OpendataAttachmentsSerializer(many=True, read_only=True)
    files_count = IntegerField()
    class Meta:
        model = Opendata
        fields = ['title', 'link', 'ilova', 'files_count', 'attachments']
