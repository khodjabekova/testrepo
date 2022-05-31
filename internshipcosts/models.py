from solo.models import SingletonModel
from enum import Enum
from django.db import models
from accounts.models import CustomUser
from baseapp.models import BaseModel
from config.regions import RegionsEnum
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import make_password

User = settings.AUTH_USER_MODEL


def intern_user_directory(instance, filename):
    return 'internship/intern_user/{}/{}'.format(instance.id, filename)


def internship_expenses_directory(instance, filename):
    return 'internship/intern_user/{}/{}'.format(instance.internship_expenses.intern.id, filename)


def finance_report_directory(instance, filename):
    return 'internship/intern_user/{}/{}'.format(instance.intern.id, filename)


class InternUser(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICE = (
        (MALE, 'Erkak'),
        (FEMALE, 'Ayol'),
    )
    HIGHER = 1
    POSTGRADUATE = 2
    EDU_CHOICE = (
        (HIGHER, "Oliy ta'lim"),
        (POSTGRADUATE, "Oliy ta'limdan keyingi ta'lim"),
    )

    NEW = 1
    APPROVED = 2
    REJECTED = 3
    STATUS_CHOICE = (
        (NEW, 'Yangi'),
        (APPROVED, 'Qabul qilindi'),
        (REJECTED, 'Rad etildi'),
    )
    user = models.OneToOneField(
        User, related_name='intern', on_delete=models.SET_NULL, null=True, blank=True)
    firstname = models.CharField(max_length=100, verbose_name="Ism")
    lastname = models.CharField(max_length=100, verbose_name="Familiya")
    patronymic = models.CharField(
        max_length=100, verbose_name="Otasining ismi")

    phone = models.CharField(max_length=14, verbose_name='Telefon Raqami')
    email = models.EmailField(max_length=100)
    password = models.CharField(_('password'), max_length=128)

    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICE, verbose_name='Jinsi')
    citizenship = models.CharField(max_length=150, verbose_name='Fuqarolik')
    pnfl = models.CharField(max_length=14, verbose_name='JSH SHIR')
    passport_no = models.CharField(
        max_length=9, verbose_name='Pasport seriyasi va raqami')
    date_of_birth = models.DateField(verbose_name="Tug‘ilgan sanasi")
    region = models.CharField(
        choices=[(region.name, region.value[0]) for region in RegionsEnum],
        verbose_name="Hudud", max_length=100)
    address = models.CharField(max_length=255, verbose_name='Yashash manzili')
    photo = models.ImageField(
        upload_to=intern_user_directory, verbose_name='Foto')
    work_region = models.CharField(
        choices=[(region.name, region.value[0]) for region in RegionsEnum],
        verbose_name="Ish hududi", max_length=100)
    work = models.CharField(max_length=255, verbose_name='Muassasa')
    work_address = models.CharField(
        max_length=255, verbose_name='Ish joyining manzili')
    education = models.PositiveSmallIntegerField(
        choices=EDU_CHOICE, verbose_name="Ta'lim")
    specialization = models.CharField(
        max_length=255, verbose_name='Diplom bo‘yicha mutaxassisligi')
    diplom = models.FileField(upload_to=intern_user_directory,
                              verbose_name='Mutaxassisligini tasdiqlovchi hujjat')
    phd_diplom = models.FileField(upload_to=intern_user_directory,
                                  null=True, blank=True, verbose_name='Phd diplom nusxasi')
    ielts = models.FileField(null=True, blank=True,
                             verbose_name='Ielts sertifikat nusxasi')
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICE, default=1, verbose_name="Status")
    reason = models.TextField(null=True, blank=True,
                              verbose_name="Rad etish sababi")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    reset_code = models.CharField(max_length=8, blank=True, null=True,
                                  verbose_name='Tiklash kodi')

    class Meta:
        db_table = "intern_user"
        verbose_name = 'Stajor'
        verbose_name_plural = 'Stajorlar'

    def __str__(self):
        return f"{self.lastname} {self.firstname} {self.patronymic}"

    def save(self, *args, **kwargs):
        change = False
        if not self._state.adding:
            change = True
            prev_obj = InternUser.objects.get(pk=self.id)
        else:
            self.username = self.email
            self.password = make_password(self.password)

        if change and self.status != prev_obj.status:
            if self.status == 2:  # accepted
                self.user = CustomUser.objects.create(username=self.email,
                                                      email=self.email,
                                                      firstname=self.firstname,
                                                      lastname=self.lastname,
                                                      password=self.password,
                                                      role=3)
                # super(InternUser, self).save()
                send_mail(
                    'Ilm-fanni moliyalashtirish va innovatsiyalarni qoʻllab-quvvatlash jamgʻarmasi',
                    'Siz qabul qilindingiz!',
                    settings.EMAIL_HOST_USER,
                    [self.email],
                    fail_silently=False,
                )
            elif self.status == 3:  # rejected
                send_mail(
                    'Ilm-fanni moliyalashtirish va innovatsiyalarni qoʻllab-quvvatlash jamgʻarmas',
                    "Sizning arizangiz qabul qilinmadi. Sabab: " + self.reason,
                    settings.EMAIL_HOST_USER,
                    [self.email],
                    fail_silently=False,
                )
        super(InternUser, self).save(*args, **kwargs)


class ExpensesTypeEnum(Enum):
    # __ordering__ = ['daily', 'accommodation',
    #                 'insurance', 'transport', 'internship']
    daily = ["Sutkalik xarajatlar", "Суткалик харажатлар",
             "Ежедневные расходы", "Daily expenses"]
    accommodation = ["Yashash(turar joy) xarajatlar", "Яшаш(турар жой) харажатлари",
                     "Расходы на проживание", "Accommodation expenses   "]
    insurance = ["Sug'urta xarajatlari", "Суғурта харажатлари",
                 "Страховые расходы", "Insurance costs"]
    transport = ["Transport xarajatlari", "Транспорт харажатлари",
                 "Транспортные расходы", "Transportation costs"]
    internship = ["Stajirovka xarajatlari", "Стажировка харажатлари",
                  "Стоимость стажировки", "Internship costs"]


class InternshipExpenses(BaseModel):
    NEW = 1
    APPROVED = 2
    REJECTED = 3
    STATUS_CHOICE = (
        (NEW, 'Yangi'),
        (APPROVED, 'Qabul qilindi'),
        (REJECTED, 'Rad etildi'),
    )
    slug = None
    intern = models.ForeignKey(
        InternUser, on_delete=models.CASCADE, verbose_name='Stajor')
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICE, default=1, verbose_name="Status")

    class Meta:
        db_table = "internship_expenses"
        verbose_name = 'Stajirovka xarajatlari'
        verbose_name_plural = 'Stajirovka xarajatlari'

    def __str__(self):
        return f'{self.intern} xarajatlar asosnomasi'


class CostStatementType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "internship_cost_statement_type"
        verbose_name = 'Xarajatlar asosnomasi turi'
        verbose_name_plural = 'Xarajatlar asosnomasi turlari'


class CostStatement(BaseModel):
    slug = None
    internship_expenses = models.ForeignKey(
        InternshipExpenses, related_name='cost_statements', on_delete=models.CASCADE)
    type = models.ForeignKey(
        CostStatementType, on_delete=models.PROTECT, verbose_name="Xarajat turi")
    days = models.CharField(max_length=100,
                            null=True, blank=True, verbose_name="Kunlar soni")
    currency = models.CharField(max_length=10, verbose_name='Valyuta')
    cost = models.BigIntegerField(verbose_name='Summasi')
    note = models.CharField(null=True, blank=True,
                            max_length=255, verbose_name='Izoh')
    link = models.URLField(null=True, blank=True)
    screenshot = models.FileField(
        upload_to=internship_expenses_directory, null=True, blank=True)

    class Meta:
        db_table = "internship_cost_statement"
        verbose_name = 'Xarajatlar asosnomasi'
        verbose_name_plural = 'Xarajatlar asosnomasi'

    def __str__(self):
        return f'{self.internship_expenses.intern} xarajatlar asosnomasi'


class FinancialReport(BaseModel):
    NEW = 1
    APPROVED = 2
    REJECTED = 3
    STATUS_CHOICE = (
        (NEW, 'Yangi'),
        (APPROVED, 'Qabul qilindi'),
        (REJECTED, 'Rad etildi'),
    )
    slug = None
    intern = models.ForeignKey(
        InternUser, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Stajor')
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICE, default=1, verbose_name="Status")
    file = models.FileField(
        upload_to=finance_report_directory, verbose_name='Hisobot')

    def __str__(self):
        return f'{self.intern} hisoboti'

    class Meta:
        db_table = "internship_financial_report"
        verbose_name = 'Moliyaviy hisobot'
        verbose_name_plural = 'Moliyaviy hisobot'


class InternshipCostsInfo(SingletonModel):
    id = models.IntegerField(primary_key=True, editable=False)
    cost_statement = models.FileField(
        upload_to='internship/templates', verbose_name='Xarajatlar asosnomasi namunasi')
    financial_report = models.FileField(
        upload_to='internship/templates', verbose_name='Moliyaviy hisobot namunasi')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created_by", null=True, blank=True,
                                   on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_updated_by', null=True, blank=True,
                                   on_delete=models.SET_NULL)

    class Meta:
        db_table = "internship_costs_info"
        verbose_name = 'Hisobotlar namunasi'
        verbose_name_plural = 'Hisobotlar namunasi'

    def __str__(self) -> str:
        return "Namuna"
