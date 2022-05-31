import random
import re
import string
from django.utils.text import slugify
from slugify import slugify as slug_translate


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''


def unique_slug_generator(instance, title=None, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
        slug = slug_translate(slug)
    title = ''.join(re.split(r'[‘.;!?,\']', title))
    Klass = instance.__class__
    max_length = Klass._meta.get_field('slug').max_length
    slug = slug[:max_length]

    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug[:max_length - 5],
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, title, new_slug=new_slug)
    return slug
