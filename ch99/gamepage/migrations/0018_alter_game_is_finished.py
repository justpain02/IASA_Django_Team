# Generated by Django 3.2.8 on 2021-11-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamepage', '0017_game_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='is_finished',
            field=models.CharField(default=False, max_length=5),
        ),
    ]