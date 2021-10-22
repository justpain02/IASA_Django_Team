from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_pw',
        'user_name',
        'user_email',
        'created_at',
        'updated_at'
    )
    list_display_link = (
        'user_id',
        'user_pw',
        'user_name',
        # 'user_email',
        'created_at',
        'updated_at'
    )