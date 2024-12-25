from django.urls import path

from ghsystems.apps.api.tasks.views import TaskDetail, TaskResource


app_name = 'tasks'

urlpatterns = [
    path('', TaskResource.as_view(), name='task-resource'),
    path('<id>/', TaskDetail.as_view(), name='task-detail'),
]
