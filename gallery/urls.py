from django.urls import path

from gallery import views

urlpatterns = [
    path('photo/', views.PhotoGalleryListAPIView.as_view()),
    path('photo/<slug>/', views.PhotoGalleryRetrieveAPIView.as_view()),
    path('video/', views.VideoGalleryListAPIView.as_view()),
    path('video/<slug>/', views.VideoGalleryRetrieveAPIView.as_view()),

]