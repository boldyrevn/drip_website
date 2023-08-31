from django.db import models
from django.urls import reverse


class Publication(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_pub', kwargs={'pub_id': self.pk})
