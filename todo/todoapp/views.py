from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
import datetime
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Todo, TaskType

# Create your views here.
class Default(View):
    template_name = 'default.xhtml'

    def get(self, request, *args, **kwargs):
        return render(request, "base.xhtml", { 'template_name': self.template_name })

class Hello(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('Well hello lady')

class About(View):
    author = "Pello Altadill"
    def get(self, request):
        return render(request, 'about.xhtml', {'author': self.author})


def validate_text(value):
    print("Validating value % ")
    if not "task" in value:
        raise ValidationError(_("Text %(val) must contain task word") % {"val":value})
    else:
        return value

class TodoForm(ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    task = forms.CharField(initial='class',label='Task', max_length=100, min_length=3, validators=[validate_text])

    class Meta:
        model = Todo
        fields = ['id','task']
        widgets = {'id': forms.HiddenInput()}


class Todos(View):
    form_class = TodoForm
    initial = {'task': 'Write your task'}
    template_name = 'todos.xhtml'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        todos = Todo.objects.all()
        print(todos)
        return render(request, "base.xhtml", {'template_name': self.template_name, 'form': form, 'todos': todos})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            todo = Todo(task=form.cleaned_data['task'])
            todo.save()
            print("Form is valid!!")
            return HttpResponseRedirect('/todos')

        return render(request, "base.xhtml", {'template_name': self.template_name, 'form': form})


class TodosDelete(View):
    model = Todo

    def get(self, request, id, *args, **kwargs):
        todo = Todo.objects.get(pk=id)
        todo.delete()
        print("Removed this id: %s" % (id))

        return HttpResponseRedirect('/todos')

class TodosUpdate(View):
    model = Todo
    form_class = TodoForm
    #initial = {'task': 'Write your task'}

    def get(self, request, id, *args, **kwargs):
        todo = Todo.objects.get(pk=id)
        form = self.form_class(initial={'task': todo.task, 'id': todo.id}) # by hand
        # form  = TodoForm(request.POST, instance=todo)
        print("Updating this id: %s" % (id))
        return render(request, "base.xhtml", {'template_name': 'update.xhtml', 'form': form, 'todo': todo})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            todo = Todo(id=form.cleaned_data['id'],task=form.cleaned_data['task'])
            todo.modified_at = datetime.datetime.now()
            todo.save()
            print("Form is valid!!")
            return HttpResponseRedirect('/todos')

        return render(request, "base.xhtml", {'template_name': 'update.xhtml', 'form': form})

class TaskTypeList(ListView):
    model = TaskType
    template_name = "task_type_list.xhtml" # or it defaults to tasktypes.html

class TaskTypeDetail(DetailView):
    model = TaskType
    template_name = "task_type_detail.xhtml" 

class TaskTypeCreation(CreateView):
    model = TaskType
    success_url = "/task_types"
    template_name = "task_type_form.xhtml" 
    fields = ['name', 'description']


class TaskTypeUpdate(UpdateView):
    model = TaskType
    success_url = "/task_types"
    template_name = "task_type_form.xhtml" 
    fields = ['name', 'description']


class TaskTypeDelete(DeleteView):
    model = TaskType
    template_name = "task_type_form.xhtml" 
    success_url = "/task_types"