from django.shortcuts import render, redirect
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
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

def update_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form})

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete_template.html', {'project': project})