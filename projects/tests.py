from django.test import TestCase

from projects.models import Project

# Create your tests here.

class ProjectModelTests(TestCase):

    def test_project_creation(self):
        # Test that a project can be created successfully
        project = Project.objects.create(name="Test Project")
        assert project.id is not None
        assert project.name == "Test Project"