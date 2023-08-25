from django.urls import path
from  .views import  CombatView

urlpatterns =[
    path('combat/<str:custom_monster_name>/', CombatView.as_view()),
]       