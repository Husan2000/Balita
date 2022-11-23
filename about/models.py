from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=221)

    def __str__(self):
        return self.category


class LatestPosts(models.Model):
    title = models.CharField(max_length=221)
    slug = models.SlugField()
    image = models.ImageField(upload_to='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='about')
    content = models.TextField()
