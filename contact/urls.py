from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.ContactCreateView.as_view()),
    path('error/', views.SendErrorMessageView.as_view()),
]