from django.db import models
from . import Result


class ResultPhoto(models.Model):
    url = models.CharField(max_length=1024)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.url
