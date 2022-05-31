from django.urls import path
from .views import (DepartamentChiefAPIView, DepartamentEmployeeListAPIView, DepartmentListAPIView, DepartmentRetrieveAPIView, DepartmentHierarchyAPIView, 
EmployeeRetrieveAPIView, EmployeeListAPIView, LeadershipEmployeeListAPIView, SupervisoryBoardAPIView, ChiefEmployeeListAPIView)

urlpatterns = [
    path('employees', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/leadership', LeadershipEmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/chief', ChiefEmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/<slug>', EmployeeRetrieveAPIView.as_view(),
         name='employee-detail'),
    path('', DepartmentListAPIView.as_view(), name='department-list'),
    path('hierarchy', DepartmentHierarchyAPIView.as_view(), name='department-hierarchy'),
    path('supervisory-board', SupervisoryBoardAPIView.as_view(), name='department-supervisory-board'),
    path('<slug>', DepartmentRetrieveAPIView.as_view(), name='department-detail'),
    path('<department>/employees', DepartamentEmployeeListAPIView.as_view(), name='department-detail'),
    path('<department>/chief', DepartamentChiefAPIView.as_view(), name='department-detail'),

]
