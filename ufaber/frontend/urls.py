from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/project/', views.add_project, name="add-project"),
    path('project/update/<id>', views.update_project, name="add-update"),

    # Task URL
    path('project/<p_id>/task/', views.task, name="task"),
    path('project/<p_id>/add/task/', views.add_task, name="add-task"),
    path('project/<p_id>/task/update/<t_id>', views.update_task, name="add-task"),
]