# Generated by Django 4.2.4 on 2023-08-09 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0005_remove_playertraits_player_traits_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playertraits',
            name='player',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='player_app.player'),
        ),
    ]
