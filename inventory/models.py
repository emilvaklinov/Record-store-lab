from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Album(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    stock_level = models.CharField(max_length=30)
    artist_id = models.CharField(max_length=20)
