from django.db import models
from django.urls import reverse


class Publication(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=64, db_index=True, unique=True, verbose_name='URL')
    content = models.TextField()
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('publication', kwargs={'pub_slug': self.slug})

    class Meta:
        ordering = ['-time_update', 'title']


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=64, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
