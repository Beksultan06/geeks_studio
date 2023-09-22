from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Task
from apps.todo.serializers import TaskSerializer

class ToDoAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.DestroyModelMixin,
              mixins.UpdateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
        
