from django.db import models
from django.db.models.fields import DateField
from datetime import date


class Show(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    watched = models.BooleanField(default=False)
    date_aired = models.DateField(default=date.today)
    def __str__(self):
        return self.name
   
