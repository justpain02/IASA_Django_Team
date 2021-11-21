from django.contrib import admin
from .models import Game
# Register your models here.


class GamepageAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_name', 'leader_name', 'answer')
admin.site.register(Game,GamepageAdmin)