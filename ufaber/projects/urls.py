from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),

    # Projects API
    path('project/', views.projectList, name="project"),
    path('project/details/<id>/', views.projectDetails, name="project-details"),
    path('project/create/', views.projectCreate, name="project-create"),
    path('project/update/<id>', views.projectUpdate, name="project-update"),
    path('project/delete/<id>', views.projectDelete, name="project-delete"),

    # Task API
    path('project/<p_id>/task/', views.taskList, name="task"),
    path('project/<p_id>/task/details/<t_id>/', views.taskDetails, name="task-details"),
    path('project/task/create/', views.taskCreate, name="task-create"),
    path('project/<p_id>/task/update/<t_id>', views.taskUpdate, name="task-update"),
    path('project/<p_id>/task/delete/<t_id>', views.taskDelete, name="task-delete"),
]