from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('projects/<uuid:pk>/', views.project_detail, name='project_detail'),
    path('projects/create/', views.create_project, name='create_project'),
]