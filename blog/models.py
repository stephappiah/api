from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    body = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def summary(self):
        return self.body[:10]

    def __str__(self):
        return self.title

    def generate_slug(self):
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        return f'{slugify(self.title)}-{now}'

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        super(Post, self).save(*args, **kwargs)
