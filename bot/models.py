from django.conf import settings
from django.db import models
from django.utils import timezone


class ToDo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    dead_line = models.DatTimeField(blank=True, null=True)

    def finish(self):
        self.delete()

    def __str__(self):
        return self.title