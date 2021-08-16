from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View


# Create your views here.
class DrillView(View):
    def get(self, request):
        return render(request, 'base.html')