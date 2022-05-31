from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from config.paginations import CustomPagination
from .models import Department, Employee, SupervisoryBoard
from .serializers import ChiefEmployeeSerializer, DepartmentDetailsSerializer, DepartmentSerializer, EmployeeListSerializer, EmployeeSerializer, \
    DepartmentHierarchySerializer, SupervisoryBoardSerializer
from django.db.models import Count


class DepartmentRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Department.objects.filter(is_active=True)
    serializer_class = DepartmentDetailsSerializer
    lookup_field = 'slug'


class DepartmentHierarchyAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = DepartmentHierarchySerializer

    def get_queryset(self):
        queryset = Department.objects.filter(level=0, is_active=True)
        return queryset


class SupervisoryBoardAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    serializer_class = SupervisoryBoardSerializer
    queryset = SupervisoryBoard.objects.filter(is_active=True)


class DepartmentListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Department.objects.filter(is_active=True)
    serializer_class = DepartmentSerializer


class EmployeeRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = EmployeeSerializer
    lookup_field = 'slug'


class EmployeeListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = EmployeeListSerializer


class DepartamentEmployeeListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = EmployeeListSerializer

    def get_queryset(self):
        slug = self.kwargs['department']
        department = Department.objects.get(slug=slug)
        return Employee.objects.filter(department=department, is_active=True).exclude(is_chief=True)


class DepartamentChiefAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = ChiefEmployeeSerializer

    def get_object(self):
        slug = self.kwargs['department']
        department = Department.objects.get(slug=slug)
        return Employee.objects.annotate(employee_count=Count('department__employee_list') - 1).filter(
            department=department, is_chief=True, is_active=True).first()

    def get(self, request, *args, **kwargs):

        instance = self.get_object()
        if instance:
            return super().get(request, *args, **kwargs)
        else:
            return Response(data=None, status=status.HTTP_404_NOT_FOUND)


class LeadershipEmployeeListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(leadership=True, is_active=True)


class ChiefEmployeeListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(is_chief=True, is_active=True).exclude(leadership=True)
