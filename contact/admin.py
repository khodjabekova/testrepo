from django.contrib import admin
from django.core.mail import send_mail

from .models import Contact
from config import settings


class ContactAdmin(admin.ModelAdmin):
    ordering = ('-created_at', )
    exclude = ['id']
    list_display = ['fullname', 'message', 'mail', 'created_at']
    search_fields = ['created_at', 'mail']

    def save_model(self, request, obj, form, change):
        if obj.status == Contact.ACCEPTED:
            send_mail(
                'Murojatingiz qabul qilindi',
                obj.reply,
                settings.EMAIL_HOST_USER,
                [obj.mail],
                fail_silently=False,
            )

        elif obj.status == Contact.REJECTED:
            send_mail(
                'Murojatingiz rad etildi',
                obj.reply,
                settings.EMAIL_HOST_USER,
                [obj.mail],
                fail_silently=False,
            )

        else:
            send_mail(
                "Murojatingiz ko'rib chiqilmoqda",
                "3 kun ichida ko'rib chiqiladi",
                settings.EMAIL_HOST_USER,
                [obj.mail],
                fail_silently=False,
            )

        super().save_model(request, obj, form, change)


admin.site.register(Contact, ContactAdmin)