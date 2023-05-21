from django.test import TestCase
from todoapp.models import Todo, TaskType

# Create your tests here.

class TaskTypeTestCase(TestCase):
    def setUp(self):
        TaskType.objects.create(name="Work", description="Finish stuff")
    
    def test_tasktype(self):
        task_type = TaskType.objects.get(name="Work")
        self.assertEqual(task_type.description, "Finish stuff")

class TodoTestCase(TestCase):
    def setUp(self):
        TaskType.objects.create(name="Work")
        Todo.objects.create(task="learn", status="0")
        Todo.objects.create(task="work", status="1")


    def test_todo(self):
        """Todos can be created correctly"""
        todo1 = Todo.objects.get(task="learn")
        todo2 = Todo.objects.get(task="work")
        self.assertEqual(todo1.status, "0")
