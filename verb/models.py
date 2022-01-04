from django.db import models

# Create your models here.
class Verb(models.Model):
    kr = models.CharField(max_length=100, null=False)
    jp = models.CharField(max_length=100, null=False)
    jp_hi = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    num = models.IntegerField(null=False)
    title = models.CharField(max_length=100, null=False)
    num = models.IntegerField(null=False)
    pages = models.IntegerField(null=False, default='number')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)