

# Create your views here.
from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import filters
from .serializers import ToDo,ToDoSerializer
from .permissions import IsOwnerPermissions
# Create your views here.
class ToDoAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsOwnerPermissions, )
    
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'description')
        

class ToDoAllDestroyAPIView(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsOwnerPermissions, )
    def delete(self, request, *args, **kwargs):
        todo = ToDo.objects.filter(user=request.user)
        todo = [t for t in todo.delete()]
        return Response({'delete' : 'Все таски удалены'})