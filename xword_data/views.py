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
            return redirect(f'/crossword_drill/correct_answer_reveal/{entry.id}/{clue.id}/{puzzle.id}')
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
        entry_ = Entry.objects.get(id=entry_id)
        puzzle = Puzzle.objects.get(id=puzzle_id)
        clue = Clue.objects.get(id=clue_id)
        clues = Clue.objects.filter(clue_text=clue.clue_text)
        entries = Entry.objects.all()
        hold_entry_dict = {}
        hold_entry_list = []
        count = 0
        for clue in clues:
            for entry_x in entries:
                if entry_x.id == clue.entry:
                    if len(hold_entry_list) == 0:
                        hold_entry_list.append(entry_x.entry_text)
                        count = count + 1
                        hold_entry_dict[entry_x.entry_text] = count
                    elif len(hold_entry_list) > 0:
                        if entry_x.entry_text in hold_entry_list:
                            hold_entry_list.append(entry_x.entry_text)
                            count = count + 1
                            hold_entry_dict[entry_x.entry_text] = count
                        elif entry_x.entry_text not in hold_entry_list:
                            hold_entry_list.append(entry_x.entry_text)
                            count = 1
                            hold_entry_dict[entry_x.entry_text] = count
        context = {
            'display_clue': clue,
            'puzzle': puzzle,
            'clues': clues,
            'entry_': entry_,
            'entries': hold_entry_dict,
        }
        print(context['entries'])
        print(hold_entry_list)
        return render(request, 'answer.html', context)