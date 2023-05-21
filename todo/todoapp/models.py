from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

class TaskType(models.Model):
    """A model of task type"""
    name = models.CharField("Task type", max_length=200, help_text="Enter task type")
    description = models.TextField("Description", max_length=400, help_text="Enter task type description")

class Todo(models.Model):
    """A model for todo"""
    task = models.CharField(_("task"), max_length=400, help_text=_("Enter task info"))
    active = models.BooleanField(_("active"),default=True)
    status = models.CharField(_("status"),choices=(
            ("0","To do"),
            ("1","Doing"),
            ("2", "Done"),
        ),
        max_length=1
    )
    created_at = models.DateTimeField(_("created_at"), auto_now=True)
    modified_at = models.DateTimeField(_("modified_at"),auto_now_add=True)
    task_type = models.ForeignKey("TaskType",on_delete=models.CASCADE, default=1)

    # Other options: help_text, verbose_name, default, null(True), blank(True), primary_key (true)

    # Metadata
