# Generated by Django 3.2.8 on 2021-11-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamepage', '0018_alter_game_is_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='is_finished',
        ),
        migrations.AddField(
            model_name='game',
            name='game_finished',
            field=models.IntegerField(default=0),
        ),
    ]