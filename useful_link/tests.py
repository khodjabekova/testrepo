import os

from django.core.files.uploadedfile import SimpleUploadedFile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()
from django.urls import reverse
from rest_framework import status
from accounts.models import CustomUser
from useful_link.serializers import UsefulLinkListSerializer, UsefulLinkDetailSerializer

from django.test import TestCase, Client

from useful_link.models import UsefulLink

client = Client()


class TestUsefulLinkViews(TestCase):

    def test_get_all_novels(self):
        response = client.get(reverse('useful-links'))
        objects = UsefulLink.objects.all()
        serializer = UsefulLinkListSerializer(objects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_details(self):
        object = UsefulLink.objects.all().first()
        serializer = UsefulLinkDetailSerializer(object)
        response = self.client.get(reverse('useful-link-detail', kwargs={'slug': object.slug}))
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
        print(serializer.data)


class TestUsefulLinkModels(TestCase):
        def setUp(self):
            self.user1 = CustomUser.objects.create_user(
                username="xan1",
                email="xan@gmail.com",
                password="xanxanxan123"
            )

            path = "C:\\Users\\xan\\Downloads\\clock.png"
            self.image = SimpleUploadedFile(name='clock.png', content=open(path, 'rb').read(), content_type='image/png')

            self.useful_link1 = UsefulLink.objects.create(
                created_by=self.user1,
                title="testTitle1",
                url="https://xan.uz",
                image=self.image,
            )

        def test_useful_link_create(self):
            self.object = UsefulLink.objects.create(
                created_by=self.user1,
                title="testTitle1",
                url="https://xan.uz",
                image=self.image,
            )
            object1 = UsefulLink.objects.get(pk=self.object.id)
            self.assertEqual(self.object.title, object1.title)

        def test_useful_link_update(self):
            self.object = UsefulLink.objects.create(
                created_by=self.user1,
                title="testTitle1",
                url="https://xan.uz",
                image=self.image,
            )
            object1 = UsefulLink.objects.filter(title="testTitle1").update(title="titleUpdate")
            test = UsefulLink.objects.filter(title="testTitle1").update(title='Everything is the same')
            print(test.title)
            # self.assertEqual(object1.title, "titleUpdate")

        def test_delete_useful_link(self):
            object = UsefulLink.objects.get(slug="salom")
            object.delete()

        def test_slug_creation(self):
            self.assertEqual(self.useful_link1.slug, 'testtitle1')
