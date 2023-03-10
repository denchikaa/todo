
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# Create your views here.

from .serializers import User,UserSerializer,UserRegisterSerializer,UserDetail


class UserAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.action in ('create', ):
            return UserRegisterSerializer
        if self.action in ('retrieve', ):
            return UserDetail
            
        return UserSerializer
