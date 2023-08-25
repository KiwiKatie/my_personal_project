from django.urls import path, include
from .views import  PlayerTraitsView, GameProgressView, CreatePlayerView, StoryAndChoices

urlpatterns = [
    path('traits/', PlayerTraitsView.as_view()),
    path('progress/', GameProgressView.as_view()),
    path('create/', CreatePlayerView.as_view()),
    path('story/', StoryAndChoices.as_view()),
]