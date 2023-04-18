from django.db import models
from apps.users.models import User

class Todo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_todo',
        verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание"
    )
    
    is_completed = models.BooleanField(
        default=False,
        verbose_name="Завершено"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField(
        upload_to='todo_images',
        verbose_name='Фотография'
    )

    def __str__(self):
        return f'{self.title} {self.user}' 

    class Meta:
        verbose_name = "Список дел"
        verbose_name_plural = "Список дел"
        
