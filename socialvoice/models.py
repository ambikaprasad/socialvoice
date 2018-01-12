from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    message = models.TextField()

