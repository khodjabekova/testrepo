import sys
from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.templatetags.static import static
from django.utils.functional import lazy
import string
import random
from django.utils.text import slugify
from slugify import slugify as slug_translate

static_lazy = lazy(static, str)
import re
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, title, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(title, allow_unicode=True)
        slug = slug_translate(slug)
    title = ''.join(re.split(r'[‘.;!?,\']', title))
    Klass = instance.__class__
    max_length = Klass._meta.get_field('slug').max_length
    slug = slug[:max_length]
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug[:max_length - 5], randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, title, new_slug=new_slug)
    return slug


def compressImage(image):
    try:
        im = Image.open(image)
        im.verify()
    except Exception:
        return None

    im = Image.open(image)
    extension = im.format.lower()
    im_io = BytesIO()

    if extension == 'jpg' or extension == 'jpeg':
        im.save(im_io, format='JPEG', optimize=True, quality=50)
        jpg = InMemoryUploadedFile(im_io, 'ImageField', "%s.jpeg" % image.name.split(
            '.')[0], 'image/jpeg', sys.getsizeof(image), None)
        return jpg
    elif extension == 'png':
        im.save(im_io, format='PNG', optimize=True, quality=50)
        png = InMemoryUploadedFile(im_io, 'ImageField', "%s.PNG" % image.name.split(
            '.')[0], 'image/png', sys.getsizeof(image), None)
        return png
    elif extension == 'webp':
        im.save(im_io, format='WEBP', optimize=True, quality=50)
        webp = InMemoryUploadedFile(im_io, 'ImageField', "%s.webp" % image.name.split(
            '.')[0], 'image/webp', sys.getsizeof(image), None)
        return webp
