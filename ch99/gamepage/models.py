from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    room_name = models.CharField('방 이름',max_length=30)
    leader_name = models.CharField('방장',max_length=30)
    people_num = models.IntegerField('사람수', default=0)
    answer = models.CharField('정답',max_length=30 , default=0)
    
    def get_absolute_url(self):
        return reverse('list')

    
    def __str__(self):
        return self.title