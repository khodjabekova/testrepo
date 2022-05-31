"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from . import views as img_views

schema_view = get_schema_view(
    openapi.Info(
        title="InnoFund API",
        default_version='v1',
        description="InnoFund",
        license=openapi.License(name="Technocorp"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],
    url='https://back.innofund.technocorp.uz/',
    # url='http://127.0.0.1:8000/',
)
urlpatterns = [
    path('admin/', admin.site.urls),


    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=10), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
    path('summernote/', include('django_summernote.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('upload_image/', img_views.upload_image),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    path('api/about/', include('about.urls')),
    path('api/menu/', include('menu.urls')),
    path('api/useful-links/', include('useful_link.urls')),
    path('api/vacancy/', include('vacancy.urls')),
    path('api/internship/', include('internship.urls')),
    path('api/opendata/', include('opendata.urls')),
    path('api/gallery/', include('gallery.urls')),
    path('api/departments/', include('department.urls')),
    path('api/menu/', include('menu.urls')),
    path('api/useful-links/', include('useful_link.urls')),
    path('api/vacancy/', include('vacancy.urls')),
    path('api/equipments/', include('equipments.urls')),
    path('api/post/', include('post.urls')),
    path('api/contacts/', include('contact.urls')),
    path('api/faq/', include('faq.urls')),
    path('api/statistics/', include('statisticsapp.urls')),
    path('api/events/', include('event.urls')),
    path('api/internshipcosts/', include('internshipcosts.urls')),
)
