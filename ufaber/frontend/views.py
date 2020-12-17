from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def add_project(request):
    return render(request, 'frontend/project_add.html')

def update_project(request, id):
    return render(request, 'frontend/edit_project.html', {'id':id})


# Task View
def task(request, p_id):
    return render(request, 'frontend/task_list.html', {'p_id':p_id})

def add_task(request, p_id):
    return render(request, 'frontend/add_task.html', {'p_id':p_id})

def update_task(request, t_id, p_id):
    context = {
        'p_id': p_id,
        't_id': t_id
    }
    return render(request, 'frontend/edit_task.html', context)
