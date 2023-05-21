from django.test import TestCase
from django.test import Client
from todoapp.models import Todo, TaskType
from todoapp.views import Todos, TodosDelete

# Create your tests here.
## Model tests
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

## View tests
client = Client(enforce_csrf_checks=True)

class TodoViewsTestCase(TestCase):
    fixtures = ["todoapp/fixtures/todo.json"]
    def setUp(self):
        TaskType.objects.create(name="Work")

    def test_todo_all(self):
        """Todos are shown"""
        response = client.get("/todos")

        self.assertIs(response.resolver_match.func.view_class, Todos)
        self.assertEqual(response.status_code, 200)

        self.assertIn(b"Finish this Django site", response.content)
        self.assertIn(b"Write your task 1", response.content)

    def test_todo_delete(self):
        """Todo is deleted"""
        response = client.get("/todos")

        self.assertIn(b"Finish this Django site", response.content)

        response = client.get("/todos/delete/2")  

        self.assertIs(response.resolver_match.func.view_class, TodosDelete)
        self.assertEqual(response.status_code, 302)

        response = client.get("/todos")

        self.assertNotIn(b"Write your task 1", response.content)