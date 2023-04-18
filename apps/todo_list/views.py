from rest_framework.viewsets import GenericViewSet
from apps.todo_list.models import Todo
from apps.todo_list.serializers import TodoSerializer
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin,DestroyModelMixin,ListModelMixin,RetrieveModelMixin
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework import filters


class TodoAPIViewSet(GenericViewSet,
                     ListModelMixin,
                     CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     RetrieveModelMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'description')

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class ToDoAllDeleteAPIViewSet(DestroyAPIView):
    queryset = Todo.objects.all()
    
    def delete(self, request, *args, **kwargs):
        todo = Todo.objects.filter(user=request.user)
        todo = [t for t in todo.delete()]
        return Response({'delete' : 'Все задания удалены'})