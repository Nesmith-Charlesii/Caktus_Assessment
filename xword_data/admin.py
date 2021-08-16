from django.contrib import admin
from .models import Puzzle, Entry, Clue

# Register your models here.
admin.site.register(Puzzle)
admin.site.register(Entry)
admin.site.register(Clue)