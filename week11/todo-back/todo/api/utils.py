import functools
import time
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import PermissionDenied
from django.template.loader import render_to_string
from api.models import Task

def user_can_read_task(task, user):
    return task.task_list.group in user.groups.all() or user.is_staff


def todo_get_backend(task):
    '''returns a mail backend for some task'''
    mail_backends = getattr(settings, "TODO_MAIL_BACKENDS", None)
    if mail_backends is None:
        return None

    task_backend = mail_backends[task.task_list.slug]
    if task_backend is None:
        return None

    return task_backend


def toggle_task_completed(task_id: int) -> bool:
    try:
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        return True
    except Task.DoesNotExist:
        # FIXME proper log message
        print("task not found")
        return False