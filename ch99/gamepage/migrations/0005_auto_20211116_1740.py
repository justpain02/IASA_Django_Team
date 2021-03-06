# Generated by Django 3.2.8 on 2021-11-16 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamepage', '0004_auto_20211104_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='유저', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='game',
            name='people_num',
        ),
        migrations.AddField(
            model_name='game',
            name='people_num',
            field=models.ManyToManyField(blank=True, default=0, related_name='참여수', to=settings.AUTH_USER_MODEL),
        ),
    ]
