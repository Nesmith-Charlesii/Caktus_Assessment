from . import views
from django.urls import path

app_name = 'xword_data'
urlpatterns = [
    path('', views.index, name='index')
]
