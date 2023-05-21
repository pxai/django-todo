"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from .views import Default
from .views import Hello
from .views import About
from .views import Todos
from .views import TodosUpdate
from .views import TodosDelete
from .views import TaskTypeList, TaskTypeDetail, TaskTypeCreation, TaskTypeUpdate, TaskTypeDelete
# Other option: from . import views and then views.task_type.TaskTypeList

urlpatterns = [
    # path('todo/', include('todo.urls')),
    path('', Default.as_view(), name='home'),
    path('hello', Hello.as_view(), name='hello'),
    path('about', About.as_view(), name='about'),
    path('todos', Todos.as_view(), name='todos'),
    path('todos/update/<int:id>', TodosUpdate.as_view(), name='update_todo'),
    path('todos/delete/<int:id>', TodosDelete.as_view(), name='delete_todo'),
    path('task_types', TaskTypeList.as_view(), name='task_type'),
    path('task_types/<int:pk>', TaskTypeDetail.as_view(), name='task_type_detail'),
    path('task_types/new', TaskTypeCreation.as_view(), name='task_type_new'),
    path('task_types/update/<int:pk>', TaskTypeUpdate.as_view(), name='task_type_update'),
    path('task_types/delete/<int:pk>', TaskTypeDelete.as_view(), name='task_type_delete')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#    
#    
#    path('^task_types/new$', TaskTypeCreation.as_view(), name='new'),
#    path('^task_types/update/(?P<pk>\d+)$', TaskTypeUpdate.as_view(), name='update'),
#    path('^task_types/delete/(?P<pk>\d+)$', TaskTypeDelete.as_view(), name='delete'),