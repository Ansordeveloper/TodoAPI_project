# Generated by Django 4.2 on 2023-04-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Список дел', 'verbose_name_plural': 'Список дел'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Завершено'),
        ),
    ]
