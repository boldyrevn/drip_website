from django.db import models
from django.urls import reverse


class Publication(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('publication', kwargs={'pub_id': self.pk})

    class Meta:
        ordering = ['-time_update', 'title']


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
