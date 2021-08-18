from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
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
            'puzzle': puzzle,
            'reveal_click': False
        }
        return render(request, 'base.html', context)

    def post(self, request, entry_id, clue_id, puzzle_id):
        guess = request.POST['answer']
        entry = Entry.objects.get(id=entry_id)
        puzzle = Puzzle.objects.get(id=puzzle_id)
        clue = Clue.objects.get(id=clue_id)
        if guess == entry.entry_text:
            return HttpResponseRedirect(f'/crossword_drill/correct_answer_reveal/{entry.id}/{clue.id}/{puzzle.id}')
        else:
            messages.error(request, 'Answer is incorrect. Give it another go!')
            context = {
                'display_clue': clue,
                'entry': entry,
                'puzzle': puzzle,
                'reveal_click': False
            }
            return render(request, 'base.html', context)


def escape_hatch(request, entry_id, clue_id, puzzle_id):
    entry = Entry.objects.get(id=entry_id)
    puzzle = Puzzle.objects.get(id=puzzle_id)
    clue = Clue.objects.get(id=clue_id)
    context = {
        'display_clue': clue,
        'entry': entry,
        'puzzle': puzzle,
        'reveal_click': True
    }
    return render(request, 'base.html', context)


class AnswerView(View):
    def get(self, request, entry_id, clue_id, puzzle_id):
        entry = Entry.objects.get(id=entry_id)
        puzzle = Puzzle.objects.get(id=puzzle_id)
        clue = Clue.objects.get(id=clue_id)
        clues = Clue.objects.filter(clue_text=clue.clue_text)
        entries = Entry.objects.all()
        print(type(clues))
        context = {
            'display_clue': clue,
            'entry': entry,
            'puzzle': puzzle,
            'clues': clues,
            'entries': entries
        }
        return render(request, 'answer.html', context)