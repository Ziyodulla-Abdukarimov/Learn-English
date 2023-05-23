from django.db import models
from ckeditor.fields import RichTextField


class UZVerb(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField()

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(UZVerb, on_delete=models.CASCADE, related_name='choice')
    content = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content
