from django.db import models


# Create your models here.
class Puzzle(models.Model):
    title = models.CharField(max_length=255),
    date = models.DateField(),
    byline = models.CharField(max_length=255),
    publisher = models.CharField(max_length=12)


class Entry(models.Model):
    pass


class Clue(models.Model):
    pass