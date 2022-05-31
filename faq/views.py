from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from config.paginations import CustomPagination
from faq.models import Faq
from faq.serializers import FaqSerializer


class FaqListView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Faq.objects.filter(is_active=True)
    serializer_class = FaqSerializer
