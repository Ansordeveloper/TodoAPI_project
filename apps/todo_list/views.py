from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from apps.todo_list.models import Todo
from apps.todo_list.serializers import TodoSerializer
from rest_framework import filters

class TodoAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'description')

class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoUpdateAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # permission_classes = (IsOwnerPermissions, )

class TodoDestroyAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    # permission_classes = (IsOwnerPermissions, )

class TodoAllDestroyAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    # permission_classes = (IsOwnerPermissions, )

    def delete(self, request, *args, **kwargs):
        todo = Todo.objects.filter(user=request.user)
        todo = [t for t in todo.delete()]
        return Response({'delete' : 'Все такски удалены'})