from django.urls import path

from internship import views

urlpatterns = [
    path('', views.InternListView.as_view()),
    path('<slug>/', views.InternDetailView.as_view()),
]
