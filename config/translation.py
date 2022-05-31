from modeltranslation.translator import register, TranslationOptions
from about.models import About
from faq.models import Faq
from gallery.models import PhotoGallery, VideoGallery
from internship.models import Intern
from internshipcosts.models import CostStatementType, InternshipCostsInfo
from opendata.models import Opendata, OpendataAttachments
from department.models import Department, Employee, SupervisoryBoard
from menu.models import Menu
from equipments.models import Equipment, Type
from useful_link.models import UsefulLink
from vacancy.models import Vacancy
from post.models import Post, PostAttachments
from event.models import Event, EventType
from statisticsapp.models import Country, ScienceField, EquipmentPurchaseStatistics, RegionSight


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('description', 'address', 'transport')
    required_languages = ('uz',)


@register(CostStatementType)
class CostStatementTypeTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(InternshipCostsInfo)
class InternshipCostsInfoTranslationOptions(TranslationOptions):
    fields = ('cost_statement', 'financial_report',)

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'working_hours',
              'biography', 'responsibilities')
    required_languages = {'uz': ('name',)}


@register(SupervisoryBoard)
class SupervisoryBoardTranslationOptions(TranslationOptions):
    fields = ('name', 'position',)


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'note')
    required_languages = {'uz': ('title',)}


@register(UsefulLink)
class UsefulLinkTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = {'uz': ('title', 'content')}


@register(Intern)
class InternTranslationOptions(TranslationOptions):
    fields = ['name', 'position', 'place', 'biography', ]


@register(Opendata)
class OpendataTranslationOptions(TranslationOptions):
    fields = ['title', 'ilova']


@register(OpendataAttachments)
class OpendataAttachmentsTranslationOptions(TranslationOptions):
    fields = ('name', 'file')
    required_languages = ('uz',)


@register(PhotoGallery)
class PhotoGalleryTranslationOptions(TranslationOptions):
    fields = ['name']


@register(VideoGallery)
class VideoGalleryTranslationOptions(TranslationOptions):
    fields = ['name']


@register(Equipment)
class EquipmentTranslationOptions(TranslationOptions):
    fields = ('name', 'content')
    required_languages = ('uz',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = {'uz': ('title', 'content')}


@register(PostAttachments)
class PostAttachmentsTranslationOptions(TranslationOptions):
    fields = ('name', 'file')
    required_languages = ('uz',)


# @register(Tags)
# class TagsTranslationOptions(TranslationOptions):
#     fields = ('name',)
#     required_languages = ('uz',)


@register(Type)
class TypeTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('uz',)


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ['question', 'answer']


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('uz',)


@register(ScienceField)
class ScienceFieldTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('uz',)


@register(Event)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'main_topic', 'responsible_org', 'address')
    required_languages = ('uz',)


@register(EventType)
class MenuTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('uz',)


@register(RegionSight)
class RegionSightTranslationOptions(TranslationOptions):
    fields = ['title', 'content']
    required_languages = ('uz',)


@register(EquipmentPurchaseStatistics)
class EquipmentPurchaseStatisticsTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('uz',)
