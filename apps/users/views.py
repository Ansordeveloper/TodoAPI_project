from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from apps.users.serializers import UserSerializer, UserRegisterSerializer
from apps.users.models import User
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import filters



# Create your views here.
class UserAPIViewSet(GenericViewSet,
                     ListModelMixin,
                     RetrieveModelMixin,
                     CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('username' , 'email', 'phone_number', 'age')

    def get_serializer_class(self):
        if self.action in ('create', ):
            return UserRegisterSerializer
        return UserSerializer