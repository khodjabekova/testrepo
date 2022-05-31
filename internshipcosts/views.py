from accounts.models import CustomUser
from config.utils import random_string_generator
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.http import JsonResponse
from django.middleware import csrf
from django.utils.translation import get_language
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from django.http import HttpResponse
from .excel_utils import InternshipExpensesExcel
import json


from .models import CostStatementType, FinancialReport, InternUser, InternshipCostsInfo, InternshipExpenses
from . import serilaizers


User = settings.AUTH_USER_MODEL


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }


class InternshipExpensesExcelAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk):
        response = HttpResponse(content_type='application/force-download')
        response['Content-Disposition'] = 'attachment;filename=xarajatlar_asosnomasi.xlsx'
        xlsx_data = InternshipExpensesExcel(object_id=pk)
        response.write(xlsx_data)
        return response

class InternUserCreateAPIView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serilaizers.InternUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response = Response()
            serialized = self.serializer_class(user)
            response.data = {"user": serialized.data}
            lang = get_language()
            if lang == 'uz':
                send_mail(
                    "Ilm-fanni moliyalashtirish va innovatsiyalarni qoʻllab-quvvatlash jamgʻarmasi",
                    "Sizning arizangiz qabul qilindi. Аrizangiz masʼul xodimlar tomonidan 10 ish kunida oʼrganib chiqilib, tegishli xulosa elektron pochtangizga yuboriladi.",
                    settings.EMAIL_HOST_USER,
                    [serializer.data['email']],
                    fail_silently=False,
                )
            elif lang == 'uzb':
                send_mail(
                    "Илм-фанни молиялаштириш ва инновацияларни қўллаб-қувватлаш жамғармаси",
                    "Сизнинг аризангиз қабул қилинди. Аризангиз масъул ходимлар томонидан 10 иш кунида ўрганиб чиқилиб, тегишли хулоса электрон почтангизга юборилади.",
                    settings.EMAIL_HOST_USER,
                    [serializer.data['email']],
                    fail_silently=False,
                )
            elif lang == 'ru':
                send_mail(
                    "Фонд финансирования науки и поддержки инноваций",
                    "Ваша заявка принята и будет рассмотрено ответственными сотрудниками в течение 10 рабочих дней и соответствующее заключение будет отправлено на Вашу электронную почту.",
                    settings.EMAIL_HOST_USER,
                    [serializer.data['email']],
                    fail_silently=False,
                )
            else:
                send_mail(
                    "Fund funding for science and support innovation",
                    "Your application is accepted. It will be considered by responsible specialists within 10 working days and the corresponding conclusion will be sent to your e-mail.",
                    settings.EMAIL_HOST_USER,
                    [serializer.data['email']],
                    fail_silently=False,
                )

            return response
        else:
            return Response({
                'status': 400,
                'message': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveDeleteListApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = InternUser.objects.all()
    serializer_class = serilaizers.InternUserSerializer

    def get_object(self):
        user = self.request.user
        obj = InternUser.objects.get(email=user.email)
        return obj

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            try:
                obj = serializer.update(
                    instance=instance, validated_data=serializer.validated_data)
                return Response({
                    'status': 201,
                    'message': 'Succesfully created',
                    'data': self.serializer_class(obj).data,
                }, status=status.HTTP_201_CREATED)
            except:
                return Response({
                    'status': 400,
                    'message': 'Error while creating',
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': 400,
                'message': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordApiView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = serilaizers.ChangePasswordSerializer

    def get_object(self):
        user = self.request.user
        obj = InternUser.objects.get(email=user.email)
        return obj

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(status=status.HTTP_200_OK)


class LoginView(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def post(self, request, format=None):

        response = Response()
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value=data["access_token"],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    # max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_MAX_AGE'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                response.set_cookie(
                    settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                    data["refresh_token"],
                    httponly=True,
                    expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                    # max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_MAX_AGE'],
                )
                csrf.get_token(request)
                response.data = {"Success": "Login successfully"}
                return response
            else:
                return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid": "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)


class RefreshView(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def get(self, request, format=None):
        refresh_token = request.COOKIES.get(
            settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'])
        if refresh_token is None:
            raise AuthenticationFailed(
                'Authentication credentials were not provided.')

        token = RefreshToken(refresh_token)
        response = Response()
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=token.access_token,
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        response.data = {"Success": "refresh successfully"}
        return response


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def logout_view(request):
    response = JsonResponse({'message': 'Logged out'})
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response


class CheckEmail(APIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def post(self, request, format=None):
        email = request.data.get('email', None)
        obj = CustomUser.objects.filter(email=email).first()
        if obj:
            return Response({
                'status': 400,
                'message': "User with this email already exists",
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': 200,
                'message': "Ok!",
            }, status=status.HTTP_200_OK)


class WhoAmIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serilaizers.InternUserSerializer

    def get_object(self):
        user = self.request.user
        obj = InternUser.objects.get(email=user.email)
        return obj


class InternCostsCreateAPIView(generics.CreateAPIView):
    """
    Foydalanuvchining xarajatlar asosnomasini yuborish
    """
    permission_classes = [IsAuthenticated]
    serializer_class = serilaizers.InternshipExpensesSerializer

    def create(self, request, *args, **kwargs):
        intern = self.request.user.intern
        data_str = request.data.pop('data', None)
        data = json.loads(data_str[0])
        files = request.FILES
        # accommodation = request.data.pop('accommodation', None)
        # insurance = request.data.pop('insurance', None)
        # transport = request.data.pop('transport', None)
        # internship = request.data.pop('internship', None)
        # files = {
        #     'daily':daily,
        #     'accommodation':accommodation,
        #     'insurance':insurance,
        #     'transport':transport,
        #     'internship':internship,
        # }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.create(
                validated_data=serializer.validated_data, intern=intern, files=files)
            return Response({
                'status': 200,
                'message': serializer.errors,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'status': 400,
                'message': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)

        # return super().create(request, *args, **kwargs)


class FinancialReportCreateAPIView(generics.CreateAPIView):
    """
    Foydalanuvchining moliyaviy hisobotini yuborish
    """
    permission_classes = [IsAuthenticated]
    serializer_class = serilaizers.FinancialReportSerializer

    def create(self, request, *args, **kwargs):

        intern = self.request.user.intern

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.create(
                validated_data=serializer.validated_data, intern=intern)
            return Response({
                'status': 201,
                'message': "Successfully saved!",
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'status': 400,
                'message': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)


class CostStatementTypeAPIView(generics.ListAPIView):
    """
    Xarajatlar asosnomasining turlari
    """
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serilaizers.CostStatementTypeSerializer
    queryset = CostStatementType.objects.all()


class InternCostsAPIView(generics.ListAPIView):
    """
    Foydalanuvchining xarajatlar asosnomalari ro'yhati kunlar bo'yicha
    """
    permission_classes = [IsAuthenticated]
    serializer_class = serilaizers.InternshipExpensesListSerializer

    def get_queryset(self):
        user = self.request.user.intern
        queryset = InternshipExpenses.objects.filter(intern=user, status=2)
        return queryset


class InternCostsDetailAPIView(generics.RetrieveAPIView):
    """
    Foydalanuvchining id bo'yicha xarajatlar asosnomasi
    """
    permission_classes = [IsAuthenticated]
    serializer_class = serilaizers.InternshipExpensesSerializer

    def get_queryset(self):
        user = self.request.user.intern
        queryset = InternshipExpenses.objects.filter(intern=user, status=2)
        return queryset


class FinancialReportAPIView(generics.ListAPIView):
    """
    Foydalanuvchining moliyaviy hisobotlar ro'yhati
    """
    permission_classes = [IsAuthenticated]
    serializer_class = serilaizers.FinancialReportSerializer

    def get_queryset(self):
        user = self.request.user.intern
        queryset = FinancialReport.objects.filter(intern=user, status=2)
        return queryset


class SendCodeApiView(generics.CreateAPIView):
    permissiion_classes = [AllowAny, ]
    serializer_class = serilaizers.SendCodeSerializer
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        user = InternUser.objects.filter(email=email).first()
        code = random_string_generator(size=6)
        if user is None:
            return Response({
                'status': 400,
                'message': "User with this email don't exists",
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.reset_code = code
            user.save()
            send_mail(
                "Ilm-fanni moliyalashtirish va innovatsiyalarni qoʻllab-quvvatlash jamgʻarmasi",
                code,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({
                'status': 200,
                'message': "OK! Sent reset code ",
            }, status=status.HTTP_200_OK)


class CheckCodeApiView(generics.CreateAPIView):
    authentication_classes = []
    serializer_class = serilaizers.CheckCodeSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        reset_code = request.data.get('reset_code', None)
        email = request.data.get('email', None)
        intern = InternUser.objects.filter(
            email=email, reset_code=reset_code).exists()
        if intern:
            user = intern.user
            response = Response()
            if user is not None:
                if user.is_active:
                    data = get_tokens_for_user(user)
                    response.set_cookie(
                        key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                        value=data["access_token"],
                        expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                        # max_age=settings.SIMPLE_JWT['ACCESS_TOKEN_MAX_AGE'],
                        secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                        httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                        samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                    )
                    response.set_cookie(
                        settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                        data["refresh_token"],
                        httponly=True,
                        expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                        # max_age=settings.SIMPLE_JWT['REFRESH_TOKEN_MAX_AGE'],
                    )
                    csrf.get_token(request)
                    response.data = {"Success": "Login successfully"}
                    return response
                else:
                    return Response({"No active": "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"Invalid": "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({
                'status': 400,
                'message': 'yozgan kodingiz ayni emailga yuborilgan kod bilan mos emas'
            },
                status=status.HTTP_400_BAD_REQUEST
            )


class ResetPasswordApiView(generics.UpdateAPIView):
    authentication_classes = []
    serializer_class = serilaizers.ResetPasswordSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        password = request.data.get['password']
        user = self.request.user
        user.password = make_password(password)
        user.save()


class CostStatementTemplateView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serilaizers.CostStatementTemplateSerializer

    def get_object(self):
        try:
            obj = InternshipCostsInfo.objects.get(pk=1)
        except:
            obj = None
        return obj


class FinancialReportTemplateView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serilaizers.FinancialReportTemplateSerializer

    def get_object(self):
        try:
            obj = InternshipCostsInfo.objects.get(pk=1)
        except:
            obj = None
        return obj
