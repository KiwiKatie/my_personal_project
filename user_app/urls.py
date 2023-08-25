from django.urls import path
from .views import Sign_up, Info, Log_in, Log_out, Admin_Sign_up
urlpatterns = [
    path('signup/', Sign_up.as_view()),
    path('login/', Log_in.as_view()),
    path('logout/', Log_out.as_view()),
    path('info/', Info.as_view()),
    path('admin_sign_up/', Admin_Sign_up.as_view()),
]