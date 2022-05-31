from django.urls import path
from . import views

urlpatterns = [
    path('', views.EquipmentListAPIView.as_view(), name='equipment-list'),
    path('types/', views.EquipmentTypeListAPIView.as_view(), name='equipment-list'),
    path('regions/', views.RegionList.as_view(), name="regions"),
    path('on-slider/', views.EquipmentOnSliderListAPIView.as_view(), name="regions"),
    path('<slug>', views.EquipmentRetrieveAPIView.as_view(), name='equipment-detail'),
]
