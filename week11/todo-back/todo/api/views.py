from django.shortcuts import render
from django.http import HttpResponse

def list_lists(request):
    return render(request, 'index.html')
# Create your views here.
def list_detail(request):
    return render(request, 'list_detail.html')
def task_detail(request):
    return render(request, 'task_detail.html')