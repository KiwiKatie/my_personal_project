# Generated by Django 4.2.4 on 2023-08-09 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player_app', '0003_rename_player_playertraits_player_traits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playertraits',
            name='player_traits',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player_app.player'),
        ),
    ]
