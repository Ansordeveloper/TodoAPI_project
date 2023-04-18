from django.contrib import admin
from apps.todo_list.models import Todo

admin.site.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'created_at']
    search_fields = ['user_username', 'title', 'description', 'created_at']

