from django.db import models

class Shows(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    watched = models.BooleanField(default=False)
