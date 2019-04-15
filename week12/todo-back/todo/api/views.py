import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TaskList,Task
from django.views.decorators.csrf import csrf_exempt
from .serializers import TaskSerializer, TaskSerializer2, ProductSerializer


# Create your views here.

def index(request):
    return HttpResponse('<h1> Index page </h1>')

@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        task_list = TaskList.objects.all()
        serializer = TaskSerializer2(task_list, many=True)
        json_tasks = [a.to_json() for a in task_list]
        return JsonResponse(json_tasks, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskSerializer2(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def task_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(task_list.to_json())
    if request.method == 'GET':
        serializer = TaskSerializer(task_list)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TaskSerializer(instance=task_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = task_list.task_set.all()
    serializer = ProductSerializer(tasks, many=True)
    json_task = [a.to_json() for a in tasks]
    return JsonResponse(json_task, safe=False)