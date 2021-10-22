from django.db import models
from django.conf import settings
# 코드 참고 : https://velog.io/@keywookim/We.TIL-20-Django-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EB%A1%9C%EA%B7%B8%EC%9D%B8-%ED%8E%98%EC%9D%B4%EC%A7%80-%EA%B5%AC%ED%98%84
# https://velog.io/@fcfargo/TIL-Django-%ED%9A%8C%EC%9B%90-%EA%B0%80%EC%9E%85-%EB%B0%8F-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EC%B2%98%EB%A6%AC%ED%94%BC%EB%93%9C%EB%B0%B1
# https://arotein.tistory.com/9

from .validators import validate_email, validate_password
# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')
    user_pw = models.CharField(max_length=128, validators=[validate_password], verbose_name='유저 비밀번호')
    user_name = models.CharField(max_length=16, unique=True, verbose_name='유저 이름')
    user_email = models.EmailField(max_length=50, validators=[validate_email], verbose_name='유저 이메일')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='계정 생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='계정정보 수정일')

