from django.urls import path

from useful_link import views

urlpatterns = [
    path('', views.UsefulLinkListView.as_view()),
    # path('<slug>/', views.UsefulLinkDetailView.as_view()),
]
