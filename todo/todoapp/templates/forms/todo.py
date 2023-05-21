from django import forms
from django.forms import ModelForm
from .validators.validate_text import validate_text
from ...models.todo import Todo

class TodoForm(ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    task = forms.CharField(initial='class',label='Task', max_length=100, min_length=3, validators=[validate_text])

    class Meta:
        model = Todo
        fields = ['id','task']
        widgets = {'id': forms.HiddenInput()}