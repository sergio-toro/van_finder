from django.db import models


class Result(models.Model):
    title = models.CharField(max_length=500, db_index=True)
    fuel_type = models.CharField(max_length=64, blank=True, default='')
    year = models.CharField(max_length=32, blank=True, default='')
    km = models.CharField(max_length=32, blank=True, default='')
    province = models.CharField(max_length=128, blank=True, default='')
    provider = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    identifier = models.CharField(max_length=256)
    url = models.CharField(max_length=200)
    photo_url = models.CharField(max_length=1024, blank=True, null=True, default=None)
    description = models.TextField(max_length=4096, blank=True, default='')
    allow_finance = models.NullBooleanField(blank=True, null=True)
    viewed = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(default=1)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        unique_together = ('provider', 'identifier')

    def __str__(self):
        return self.title
