from django.urls import path

from . import views

urlpatterns = [
    path('all', views.FinanceInternshipAllYearsView.as_view()),
    path('years', views.FinanceInternshipYearsView.as_view()),
    path('<year>', views.FinanceInternshipByYearView.as_view()),
    ]