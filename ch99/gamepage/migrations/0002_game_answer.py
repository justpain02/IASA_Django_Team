# Generated by Django 3.1 on 2021-10-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='answer',
            field=models.CharField(default=0, max_length=30, verbose_name='정답'),
        ),
    ]
