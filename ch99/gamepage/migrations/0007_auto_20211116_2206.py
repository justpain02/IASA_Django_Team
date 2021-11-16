# Generated by Django 3.1 on 2021-11-16 22:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamepage', '0006_auto_20211116_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='people_num',
            field=models.ManyToManyField(blank=True, default=3, related_name='참여수', to=settings.AUTH_USER_MODEL),
        ),
    ]