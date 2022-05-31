import base64
from rest_framework import serializers
from .models import Department, Employee, SupervisoryBoard
from django.core.files.images import get_image_dimensions
from rest_framework_recursive.fields import RecursiveField


class EmployeeListSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(
        slug_field='name', read_only=True)
    department_slug = serializers.SlugRelatedField(source='department',
        slug_field='slug', read_only=True)
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['slug', 'name', 'email', 'phone', 'internal_number',
                  'department', 'department_slug', 'position', 'photo', ]

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            image_url = obj.thumbnail.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.thumbnail.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_str = data_base64.decode("utf-8")
                data = {
                    'src': path,
                    'width': w,
                    'height': h,
                    'base64': "data:image/jpg;base64," + byte_to_str,
                }
                return data
            except Exception:
                return None
        else:
            None


class EmployeeSerializer(EmployeeListSerializer):

    class Meta(EmployeeListSerializer.Meta):
        model = Employee
        fields = EmployeeListSerializer.Meta.fields + \
            ['biography', 'working_hours', 'responsibilities']


class ChiefEmployeeSerializer(EmployeeSerializer):
    employee_count = serializers.IntegerField()

    class Meta(EmployeeSerializer.Meta):
        fields = EmployeeSerializer.Meta.fields + ['employee_count']


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ['slug', 'name', 'index']


class DepartmentDetailsSerializer(DepartmentSerializer):
    employee_list = EmployeeListSerializer(many=True, read_only=True)
    # chief

    class Meta(DepartmentSerializer.Meta):
        model = Department
        fields = DepartmentSerializer.Meta.fields + ['employee_list']


class DepartmentHierarchySerializer(DepartmentSerializer):
    sub_departments = RecursiveField(many=True)

    class Meta(DepartmentSerializer.Meta):
        model = Department
        fields = DepartmentSerializer.Meta.fields + ['sub_departments']


class SupervisoryBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisoryBoard
        fields = ['slug', 'name', 'position']
