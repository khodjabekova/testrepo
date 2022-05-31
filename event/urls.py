from django.urls import path

from .views import EventListView, EventDetailView


urlpatterns = [
    path('', EventListView.as_view()),
    path('<slug>', EventDetailView.as_view()),
]