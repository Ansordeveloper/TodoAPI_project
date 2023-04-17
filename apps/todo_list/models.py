from django.db import models

class Todo(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=200, verbose_name='Описание'
    )
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Завершино'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Списки'
