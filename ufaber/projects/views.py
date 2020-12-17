from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, Task

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer, TaskSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Project List': '/project/',
        'Project View': '/project/details/<id>',
        'Create Project': '/project/create/',
        'Update Project': '/project/update/<id>',
        'Delete Project': '/project/delete/<id>',

        'Task List': '/project/<id>/task/',
        'Task View': '/project/<id>/task/details/<id>',
        'Create Task': '/project/task/create/',
        'Update Task': '/project/<id>/task/update/<id>',
        'Delete Task': '/project/<id>/task/delete/<id>',
    }
    return Response(api_urls)

# Projects
@api_view(['GET'])
def projectList(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def projectDetails(request, id):
    projects = Project.objects.get(id=id)
    serializer = ProjectSerializer(projects, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def projectCreate(request):
    serializer = ProjectSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def projectUpdate(request, id):
    projects = Project.objects.get(id=id)
    serializer = ProjectSerializer(instance=projects, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def projectDelete(request, id):
    projects = Project.objects.get(id=id)
    projects.delete()

    return Response("Project Successfully Deleted")

# Task
@api_view(['GET'])
def taskList(request, p_id):
    task = Task.objects.all().filter(project__id=p_id)
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request, t_id, p_id):
    task = Task.objects.get(id=t_id, project__id=p_id)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, t_id, p_id):
    task = Task.objects.get(id=t_id, project__id=p_id)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, p_id, t_id):
    task = Task.objects.get(id=t_id, project__id=p_id)
    print(task)
    task.delete()

    return Response("Project Successfully Deleted")