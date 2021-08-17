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
        entry = Entry.objects.get(id=display_clue.entry)
        puzzle = Puzzle.objects.get(id=display_clue.puzzle)
        print(entry.entry_text)
        print(puzzle.title)
        context = {
            'display_clue': display_clue,
            'entry': entry,
            'puzzle': puzzle
        }
        return render(request, 'base.html', context)

    def post(self, request, entry_id):
        guess = request.POST['guess']
        entry = Entry.objects.get(id=entry_id)
        if guess == entry.entry_text:
            return HttpResponseRedirect(reverse('xword_data:index'))


class AnswerView(View):
    pass