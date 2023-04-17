from rest_framework import serializers

from apps.todo_list.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    model = Todo
    fields = '__all__'
    