# Generated by Django 3.2.8 on 2021-11-22 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamepage', '0010_game_current_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='current_status',
            field=models.CharField(default=[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], max_length=200, validators=[django.core.validators.int_list_validator]),
        ),
    ]
