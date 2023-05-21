from django.contrib import admin
from .models import Todo, TaskType

# Register your models here.

# admin.site.register(Ad)

admin.site.register(Todo)
admin.site.register(TaskType)

class TodoAdmin(admin.ModelAdmin):
     list_display = ['id', 'task', 'status', 'task_type']
     list_filter = ['task', 'status']
     search_fields = ['task', 'status']
#     prepopulated_fields = {'slug': ('title',)}
     raw_id_fields = ['task']
#     date_hierarchy = 'publish'
     ordering = ['task', 'status']

# Register your models here.
