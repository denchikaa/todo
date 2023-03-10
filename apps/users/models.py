from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(
        verbose_name="Ваша почта",
        unique=True
    )
    phone_number = models.CharField(
        max_length=25,
        verbose_name="ваш тел.ном"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    age = models.CharField(
        max_length=2,
        verbose_name="ваш возраст"
    )
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователи",
        verbose_name_plural = "Пользователь"