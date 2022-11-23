from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=221)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=221)

    def __str__(self):
        return self.tag


class Post(models.Model):
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='posts')
    content = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comments', null=True, blank=True)
    name = models.CharField(max_length=221)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
