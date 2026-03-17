from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    title = "Projects"
    return render(request, 'projects/projects.html', {'projects': projects, 'title': title})

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    return render(request, 'projects/project_detail.html', {'project': project, 'tags': tags})

def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})