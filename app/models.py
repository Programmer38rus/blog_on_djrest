# from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
# from app.models import User as User3
from django.utils import timezone
from django.conf import settings

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    new = models.DateTimeField(default=timezone.now)


class Category(models.Model):
    url = models.SlugField
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Категории"


    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='category', null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = "Посты"

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

