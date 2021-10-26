from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 이렇게 하면 User에서 Profile 참조할 수 있고 Profile에서도 User 참조할 수 있다
    last_modified = models.DateTimeField(auto_now=True)
    profile_photo = models.ImageField(blank=True)                 # 값을 채워넣지 않아도 되는 속성.
    