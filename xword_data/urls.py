from .views import DrillView, AnswerView
from django.urls import path

app_name = 'xword_data'
urlpatterns = [
    path('', DrillView.as_view(), name="index"),
    path('clue_reveal/<int:entry_id>/', DrillView.as_view(), name="reveal_answer"),
    path('answer_reveal/', AnswerView.as_view(), name="answer_reveal")
]
