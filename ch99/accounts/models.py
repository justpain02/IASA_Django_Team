from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.CharField(max_length=30)
    user_name = models.CharField(max_length=120)
    user_password = models.CharField(max_length=31)
    user_email = models.EmailField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title