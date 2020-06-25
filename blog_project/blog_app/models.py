from django.db import models

# Create your models here.

class Post(models.Model):
    thumbnail = models.ImageField(upload_to = "static/images", null=True, blank=True)
    slug = models.SlugField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    publicacao = models.DateTimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()

    def __str__(self):
        return self.name