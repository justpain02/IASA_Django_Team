from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

def default_button_dict():
    return {
        "a" : False,
        "b" : False,
        "c" : False,
        "d" : False,
        "e" : False,
        "f" : False,
        "g" : False,
        "h" : False,
        "i" : False,
        "j" : False,
        "k" : False,
        "l" : False,
        "m" : False,
        "n" : False,
        "o" : False,
        "p" : False,
        "q" : False,
        "r" : False,
        "s" : False,
        "t" : False,
        "u" : False,
        "v" : False,
        "w" : False,
        "x" : False,
        "y" : False,
        "z" : False
    }

class Game(models.Model):
    room_name = models.CharField('방 이름',max_length=30)
    leader_name = models.CharField('방장',max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='유저', blank=True, null=True)
    people_num = models.ManyToManyField(settings.AUTH_USER_MODEL, default=0, blank=True, related_name='참여수')
    answer = models.CharField('정답',max_length=30 , default="answer")
    button_status = models.JSONField(default = default_button_dict)
    hangman_status = models.IntegerField(default=1)
    game_finished = models.IntegerField(default=0)
    def get_absolute_url(self):
        return reverse('list')

    
    def __str__(self):
        return self.room_name