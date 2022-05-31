from django.urls import path

from opendata import views

urlpatterns = [
    path('', views.OpendataListView.as_view()),
    path('bymenu/<menu>', views.OpendataByMenuListView.as_view()),
    path('<slug>/', views.OpendataDetailView.as_view()),
]
