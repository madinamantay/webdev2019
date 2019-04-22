import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TaskList,Task
from django.views.decorators.csrf import csrf_exempt
from .serializers import TaskListSerializer, TaskListSerializer2, ProductSerializer, TaskListSerializer


# Create your views here.

def index(request):
    return HttpResponse('<h1> Index page </h1>')

@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)

@csrf_exempt
def task_detail(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(tasklist)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=tasklist, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        tasklist.delete()
        return JsonResponse({})


@csrf_exempt
def tasks(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = tasklist.task_set.all()
    serializer = ProductSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)