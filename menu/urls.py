from django.urls import path
from .views import MenuListAPIView, MenuRetrieveAPIView, MenuRootAPIView, SubMenuAPIView

urlpatterns = [
    path('', MenuListAPIView.as_view(), name='menu-list'),
    path('root', MenuRootAPIView.as_view(), name='menu-list'),
    path('<slug>', MenuRetrieveAPIView.as_view(), name='menu-detail'),
    path('<slug>/submenu', SubMenuAPIView.as_view(), name='menu-detail'),
]
