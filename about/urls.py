from django.urls import path
from .views import AboutAPIView, AboutContactAPIView, AboutSocialLinksAPIView


urlpatterns = [
    path('', AboutAPIView.as_view(), name='about'),
    path('contacts', AboutContactAPIView.as_view(), name='about-contact'),
    path('social-links', AboutSocialLinksAPIView.as_view(), name='social-links'),
]
