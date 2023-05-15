from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=500)
    body = RichTextField()

    def __str__(self):
        return self.title


class Recourse(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=200)
    file = models.FileField(upload_to='recourse/')

    def __str__(self):
        return self.title
