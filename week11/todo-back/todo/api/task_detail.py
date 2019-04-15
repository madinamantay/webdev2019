import datetime

from api.models import Task
from api.utils import toggle_task_completed
from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator


def task_detail(request, task_id: int) -> HttpResponse:
    """View task details. Allow task details to be edited. Process new comments on task.
    """

    # Mark complete
    if request.POST.get("toggle_done"):
        results_changed = toggle_task_completed(task.id)
        if results_changed:
            messages.success(request, f"Changed completion status for task {task.id}")

        return redirect("todo:task_detail", task_id=task.id)

    if task.due_date:
        thedate = task.due_date
    else:
        thedate = datetime.datetime.now()

    context = {
        "task": task,
        "thedate": thedate,
    }

    return render(request, "task_detail.html", context)