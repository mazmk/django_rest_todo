from rest_framework import viewsets
from todos.models import Task
from todos.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class TodoViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

