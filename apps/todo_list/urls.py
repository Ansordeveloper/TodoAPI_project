from django.urls import path
from apps.todo_list.views import TodoAPIView,TodoCreateAPIView,TodoUpdateAPIView,TodoDestroyAPIView,TodoAllDestroyAPIView

urlpatterns = [
    path('api/', TodoAPIView.as_view()),
    path('api/todo/create/', TodoCreateAPIView.as_view()),
    path('api/todo/update/<int:pk>/', TodoUpdateAPIView.as_view()),
    path('api/todo/destroy/<int:pk>/', TodoDestroyAPIView.as_view()),
    path('api/todo/destroy/all/', TodoAllDestroyAPIView.as_view())
]