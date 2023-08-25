
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/player/', include('player_app.urls')),
    path('api/v1/inventory/', include('inventory_app.urls')),
    path('api/v1/user/', include('user_app.urls')),
    path('api/v1/monster/', include('monster_app.urls')),
]
