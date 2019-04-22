from django.contrib import admin
from .models import TaskList, Task


admin.site.register(Task)
@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')