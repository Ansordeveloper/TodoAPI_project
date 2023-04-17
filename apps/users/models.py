from django.db import models

class User(models.Model):
    username = models.CharField(
        max_length=100,
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(
        verbose_name='Почта',
        unique=True
    )
    phone_number = models.CharField(
        max_length=200,
        verbose_name='Телефонный номер',
        blank=True, null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='Возраст',
        blank=True, null=True
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'