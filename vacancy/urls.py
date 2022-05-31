from django.urls import path

from vacancy import views

urlpatterns = [
    path('', views.VacancyListView.as_view()),
]
