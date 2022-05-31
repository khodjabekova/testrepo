from rest_framework import generics
from rest_framework.permissions import AllowAny

from config.paginations import CustomPagination

from .models import Menu
from .serializers import MenuSerializer


class MenuRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Menu.objects.filter(is_active=True)
    serializer_class = MenuSerializer
    lookup_field = 'slug'


class MenuListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    # pagination_class = CustomPagination
    queryset = Menu.objects.filter(is_active=True)
    serializer_class = MenuSerializer


class MenuRootAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    # pagination_class = CustomPagination
    serializer_class = MenuSerializer

    def get_queryset(self):
        queryset = Menu.objects.filter(level=0, is_active=True)
        return queryset


class SubMenuAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    # pagination_class = CustomPagination

    serializer_class = MenuSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = Menu.objects.filter(parent__slug=slug,is_active=True)
        return queryset
