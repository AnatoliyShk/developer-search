from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project, Tag
from .forms import ProjectForm
from .utils import searchProjects

def projects(request):
    projects, search_query = searchProjects(request)
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects, results)
    projects = paginator.get_page(page)
    title = "Projects"
    return render(request, 'projects/projects.html', {'projects': projects, 'title': title, 'search_query': search_query})

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    return render(request, 'projects/project_detail.html', {'project': project, 'tags': tags})

@login_required(login_url='login')
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form})

@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete_template.html', {'project': project})