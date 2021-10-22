# Generated by Django 3.2.8 on 2021-10-22 12:56

import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')),
                ('user_pw', models.CharField(max_length=128, validators=[account.validators.validate_password], verbose_name='유저 비밀번호')),
                ('user_name', models.CharField(max_length=16, unique=True, verbose_name='유저 이름')),
                ('user_email', models.EmailField(max_length=50, validators=[account.validators.validate_email], verbose_name='유저 이메일')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='계정 생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='계정정보 수정일')),
            ],
        ),
    ]
