from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
class Game(models.Model):
    room_name = models.CharField('방 이름',max_length=30)
    leader_name = models.CharField('방장',max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='유저')
    people_num = models.ManyToManyField(settings.AUTH_USER_MODEL, default=0, blank=True, related_name='참여수')
    answer = models.CharField('정답',max_length=30 , default=0)
    
    def get_absolute_url(self):
        return reverse('list')

    
    def __str__(self):
        return self.title