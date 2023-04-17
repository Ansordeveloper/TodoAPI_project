from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView 
from apps.users.serializers import UserSerializer
from apps.users.models import User

# Create your views here.
class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer