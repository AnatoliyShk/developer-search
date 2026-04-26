from django.test import TestCase

from projects.models import Project

# Create your tests here.

class ProjectModelTests(TestCase):

    def test_project_creation(self):
        # Test that a project can be created successfully
        project = Project.objects.create(name="Test Project")
        assert project.id is not None
        assert project.name == "Test Project"

    def test_project_edit(self):
        # Test that a project can be edited successfully
        project = Project.objects.create(name="Test Project")
        project.name = "Updated Project"
        project.save()
        assert project.name == "Updated Project"
    
    def test_project_deletion(self):
        # Test that a project can be deleted successfully
        project = Project.objects.create(name="Test Project")
        project_id = project.id
        project.delete()
        assert not Project.objects.filter(id=project_id).exists()
        
    def test_project_str_representation(self):
        # Test the string representation of a project
        project = Project.objects.create(name="Test Project")
        assert str(project) == "Test Project"

    def test_project_creation_without_name(self):
        # Test that creating a project without a name raises an error
        with self.assertRaises(Exception):
            Project.objects.create(name=None)