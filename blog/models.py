from django.db import models

class Blog(models.Model):
    texti = models.CharField(max_length=2000)
