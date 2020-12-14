from django.db import models
from django.utils import timezone


class Category(models.Model):
    url = models.SlugField
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category', null=True)

    class Meta:
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
