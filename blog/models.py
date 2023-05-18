from django.db import models
from taggit.managers import TaggableManager
from accounts.models import User


class Post(models.Model):
    CATEGORIES = [('Make Up', 'Make Up'),
                  ('Last News', 'Last News'),
                  ('Learning', 'Learning'),
                  ('Photo Graphy', 'Photo Graphy')]
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.CharField(choices=CATEGORIES, max_length=20, default='unknown')
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tags = TaggableManager()

    def get_tags(self):
        """ names() is a django-taggit method, returning a ValuesListQuerySet
        (basically just an iterable) containing the name of each tag as a string
        """
        return self.tags.names()

    def __str__(self):
        return self.title
