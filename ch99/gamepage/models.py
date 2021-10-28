from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
    room_name = models.CharField('TiTLE',max_length=30)
    leader_name = models.CharField('TiTLE',max_length=30)
    people_num = models.IntegerField('TiTLE',max_length=30)
    
    def get_absolute_url(self):
        return reverse('list')