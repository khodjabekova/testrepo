from rest_framework import serializers
from .models import CostStatement, CostStatementType, FinancialReport, InternUser, InternshipCostsInfo, InternshipExpenses
from django.utils.translation import gettext_lazy as _

class InternUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternUser
        fields = ['firstname', 'lastname', 'patronymic', 'email', 'phone', 'password', 'gender',
                  'citizenship', 'passport_no', 'pnfl', 'date_of_birth', 'region', 'address',
                  'photo', 'education', 'work', 'work_region', 'work_address', 'specialization', 'diplom',
                  'phd_diplom', 'ielts']

        extra_kwargs = {
            'password': {'write_only': True}
        }



class CostStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostStatement
        fields = ['type', 'days', 'cost', 'currency', 'note', 'link', 'screenshot']


class FinancialReportSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FinancialReport
        fields = ['created_at', 'file' ]

    def create(self, validated_data, intern):
        obj = FinancialReport.objects.create(intern=intern, **validated_data)
        return obj


class CostStatementTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CostStatementType
        fields = [ 'id', 'name', ]

class InternshipExpensesListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = InternshipExpenses
        fields = [ 'id', 'created_at', ]



class InternshipExpensesSerializer(serializers.ModelSerializer):
    cost_statements = CostStatementSerializer(many=True)
    created_at = serializers.DateTimeField(read_only=True)
    # id = serializers.DateTimeField(read_only=True)
    class Meta:
        model = InternshipExpenses
        fields = [ 'id', 'created_at', 'cost_statements']

    def create(self, validated_data, intern, files):
        cost_statements = validated_data.pop("cost_statements", None)
        obj = InternshipExpenses.objects.create(intern=intern, **validated_data)
        for cs in cost_statements:
            type = cs['type']
            cost = CostStatement.objects.create(internship_expenses=obj, **cs)
            try:
                screenshot = files[type.name_uz]
                cost.screenshot = screenshot
                cost.save()
            except:
                pass

        return obj


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
        # password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user

class SendCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternUser
        fields = ['email']


class CheckCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternUser
        fields = ['email', 'reset_code']


class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternUser
        fields = ['password',
                  # 'email', 'reset_code'
                  ]


class CostStatementTemplateSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source='cost_statement')
    class Meta:
        model = InternshipCostsInfo
        fields = [ 'id', 'file', ]

class FinancialReportTemplateSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source='financial_report')
    class Meta:
        model = InternshipCostsInfo
        fields = [ 'id', 'file', ]