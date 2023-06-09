# Generated by Django 4.2 on 2023-04-18 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_age'),
        ('todo_list', '0002_alter_todo_options_alter_todo_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='image',
            field=models.ImageField(default=1, upload_to='todo_images', verbose_name='Фотография'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_todo', to='users.user', verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
