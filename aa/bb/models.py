from django.db import models

# Create your models here.

class cview(models.Model):
    cid = models.CharField(primary_key=True,max_length=10)
    cname = models.CharField(max_length=10)
    tname = models.CharField(max_length=10)