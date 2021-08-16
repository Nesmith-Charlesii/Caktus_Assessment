from .views import DrillView
from django.urls import path

app_name = 'xword_data'
urlpatterns = [
    path('', DrillView.as_view())
]
