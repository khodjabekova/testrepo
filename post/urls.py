from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='post-list'),
    path('bymenu/<menu>', views.PostListByMenuAPIView.as_view(), name='post-menu-list'),
    path('<slug>', views.PostRetrieveAPIView.as_view(), name='post-detail'),
]
