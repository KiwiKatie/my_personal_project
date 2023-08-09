from django.urls import path, include
from .views import PlayerDetails, PlayerTraitsView, GameProgress

urlpatterns = [
#     path('profile/', PlayerDetails.as_view()),
#     path('traits/', PlayerTraits.as_view()),
#     path('progress/', GameProgress.as_view()),
    path('profile/<int:player_id>/', PlayerDetails.as_view()),
    path('traits/<int:player_id>/', PlayerTraitsView.as_view()),
    path('progress/<int:player_id>/', GameProgress.as_view()),
 ]