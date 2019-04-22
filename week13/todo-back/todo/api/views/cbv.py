from ..models import TaskList
from ..serializers import TaskListSerializer2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Tasklist(APIView):
    def get(self, request):
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer2(tasklists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = TaskListSerializer2(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskDetail(APIView):
    def get_object(self, pk):
        try:
            return True, TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            return False, Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        found, res = self.get_object(pk)
        if found:
            serializer = TaskListSerializer2(res)
            return Response(serializer.data)
        return res

    def put(self,request, pk):
        found, tasklist = self.get_object(pk)
        serializer = TaskListSerializer2(instance=tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request, pk):
        found, tasklist = self.get_object(pk)
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)