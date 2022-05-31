from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from config.paginations import CustomPagination
from .models import Post
from .serializers import PostDetailSerializer, PostListSerializer
import django_filters
from django_filters import rest_framework as filters
from django.db.models import Q


class PostRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    # queryset = Post.objects.prefetch_related('images', 'attachments').filter(is_active=True)
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=['views', ])
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=200)


class PostFilter(django_filters.FilterSet):
    on_slider = filters.CharFilter(
        field_name='on_slider', method='filter_on_slider')

    content = filters.CharFilter(
        field_name='content', method='filter_content')

    year = filters.CharFilter(
        field_name='year', method='filter_year')

    month = filters.CharFilter(
        field_name='month', method='filter_month')

    date = filters.CharFilter(
        field_name='date', method='filter_date')

    class Meta:
        model = Post
        fields = ['content', 'year', 'month', 'date', 'on_slider']

    def filter_content(self, queryset, name, value):
        q = queryset.filter(Q(title__icontains=value.lower())
                            | Q(content__icontains=value.lower()))
        return q

    def filter_year(self, queryset, name, value):
        q = queryset.filter(
            pub_date__year=value)
        return q

    def filter_month(self, queryset, name, value):
        q = queryset.filter(
            pub_date__month=value)
        return q

    def filter_date(self, queryset, name, value):
        q = queryset.filter(
            pub_date=value)
        return q

    def filter_on_slider(self, queryset, name, value):
        q = queryset.filter(
            on_slider=True)
        return q


class PostListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    queryset = Post.objects.select_related('menu').filter(is_active=True)
    serializer_class = PostListSerializer
    filterset_class = PostFilter


class PostListByMenuAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    # queryset = Post.objects.select_related('menu').filter(is_active=True)
    # queryset = Post.objects.filter(is_active=True)
    serializer_class = PostListSerializer
    filterset_class = PostFilter


    def get_queryset(self):
        menu = self.kwargs['menu']
        queryset = Post.objects.filter(
            menu__slug=menu, is_active=True)
        return queryset
