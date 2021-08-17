from . import views
from .views import DrillView, AnswerView
from django.urls import path

app_name = 'xword_data'
urlpatterns = [
    path('', DrillView.as_view(), name="index"),
    path('clue_reveal/<int:entry_id>/<int:clue_id>/<int:puzzle_id>', DrillView.as_view(), name="reveal_answer"),
    path('correct_answer_reveal/', AnswerView.as_view(), name="answer_reveal"),
    path('escape-hatch/', views.escape_hatch, name="escape-hatch")
]
