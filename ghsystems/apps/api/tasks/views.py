from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ghsystems.apps.api.tasks.serializers import TaskDetailSerializer, TasksSerializer
from ghsystems.apps.tasks.models import Tasks as TasksModel


class TaskResource(ListCreateAPIView):
    http_method_names = ['get', 'post']
    serializer_class = TasksSerializer
    queryset = TasksModel.objects.all_available()


class TaskDetail(RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'patch', 'delete']
    serializer_class = TaskDetailSerializer
    lookup_field = 'id'
    queryset = TasksModel.objects.all_available()

