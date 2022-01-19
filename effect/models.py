from django.db import models


# Create your models here.
class Effect(models.Model):
    kr = models.CharField(max_length=100, null=False)
    jp_ka = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
