from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
import random
from .models import Clue, Puzzle, Entry


# Create your views here.
class DrillView(View):
    def get(self, request):
        clues = Clue.objects.all()
        display_clue = random.choice(clues)
        print(display_clue.clue_text)
        context = {
            'display_clue': display_clue
        }
        return render(request, 'base.html', context)