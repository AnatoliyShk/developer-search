from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project, Tag, Review
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects

def projects(request):
    projects, search_query = searchProjects(request)
    projects, custom_range = paginateProjects(request, projects, 2)
    title = "Projects"
    return render(request, 'projects/projects.html', {'projects': projects, 'title': title, 'search_query': search_query, 'custom_range': custom_range})

def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    review_form = ReviewForm()
    project.getVoteCount
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()
            messages.success(request, 'Your review was successfully submitted!')
            return redirect('project', pk=project.id)
    return render(request, 'projects/project_detail.html', {'project': project, 'tags': tags, 'review_form': review_form})

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