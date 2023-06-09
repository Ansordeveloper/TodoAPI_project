from rest_framework import serializers

from apps.todo_list.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'description',
                 'created_at', 'image')
        