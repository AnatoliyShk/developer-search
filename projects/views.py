from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return render(request, 'projects/projects.html')

def project_detail(request, project_id):
    return render(request, 'projects/project_detail.html', {'project_id': project_id})