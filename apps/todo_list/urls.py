from rest_framework.routers import DefaultRouter

from apps.todo_list.views import TodoAPIViewSet

router = DefaultRouter()
router.register('todo', TodoAPIViewSet, 'api_todo')

urlpatterns = router.urls



