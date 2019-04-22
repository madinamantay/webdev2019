from ..models import TaskList
from django.contrib.auth.models import User
from ..serializers import TaskListSerializer2, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class Tasklist2(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
    http_method_names = ['get']


class Tasklist(generics.ListCreateAPIView):
    # queryset = TaskList.objects.all()
    # serializer_class = TaskListSerializer2
    permission_classes = (IsAuthenticated, )
    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)
    def get_serializer_class(self):
        return TaskListSerializer2
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TasklistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer2
