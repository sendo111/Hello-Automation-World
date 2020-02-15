from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100, null=False, default='')
    author = models.CharField(max_length=50, null=False, default='')
    publisher = models.CharField(max_length=50, null=False, default='')
    finished_date = models.DateField(default=timezone.now, null=False)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    updated_at = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.title
