from django.db import models


# Create your models here.
class Puzzle(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField()
    byline = models.CharField(max_length=255)
    publisher = models.CharField(max_length=12)


class Entry(models.Model):
    entry_text = models.CharField(unique=True, max_length=50)


class Clue(models.Model):
    entry = models.IntegerField()
    puzzle = models.IntegerField()
    clue_text = models.TextField(max_length=512)
    theme = models.BooleanField(default=False)
