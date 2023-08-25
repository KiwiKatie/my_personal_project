# Generated by Django 4.2.4 on 2023-08-10 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('player_app', '0008_remove_playertraits_player_playertraits_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playertraits',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
