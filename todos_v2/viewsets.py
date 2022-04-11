from rest_framework import viewsets
from todos.models import Task
from todos.serializers import TaskSerializer



class TodoViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

