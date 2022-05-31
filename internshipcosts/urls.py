from django.urls import path

from . import views

urlpatterns = [
    path('registration', views.InternUserCreateAPIView.as_view()),
    path('change_password/', views.ChangePasswordApiView.as_view(), name='change-password'),
    path('update', views.UserRetrieveDeleteListApiView.as_view()),
    path('login', views.LoginView.as_view(), name='login'),
    path('refresh-token/', views.RefreshView.as_view(), name="refresh"),
    path('logout', views.logout_view, name="logout"),
    path('check-email', views.CheckEmail.as_view()),
    path('whoami', views.WhoAmIView.as_view()),
    path('costs/type', views.CostStatementTypeAPIView.as_view()),
    path('costs', views.InternCostsAPIView.as_view()),
    path('costs/create', views.InternCostsCreateAPIView.as_view()),
    path('costs/<pk>/download', views.InternshipExpensesExcelAPIView.as_view()),
    path('costs/<pk>', views.InternCostsDetailAPIView.as_view()),
    path('sendcode/', views.SendCodeApiView.as_view()),
    path('checkcode/', views.CheckCodeApiView.as_view()),
    path('password_reset/', views.ResetPasswordApiView.as_view()),
    path('finance', views.FinancialReportAPIView.as_view()),
    path('finance/create', views.FinancialReportCreateAPIView.as_view()),
    path('template/coststatement', views.CostStatementTemplateView.as_view()),
    path('template/financereport', views.FinancialReportTemplateView.as_view()),

]
