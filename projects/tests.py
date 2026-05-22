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
            
    def test_project_list(self):
        # Test that a list of projects can be retrieved successfully
        Project.objects.create(name="Project 1")
        Project.objects.create(name="Project 2")
        projects = Project.objects.all()
        assert len(projects) == 2

    def test_project_creation_with_valid_name(self):
        # Test that creating a project with a valid name works
        project = Project.objects.create(name="Valid Project")
        assert project.id is not None
        assert project.name == "Valid Project"
    
    def test_project_creation_with_empty_name(self):
        # Test that creating a project with an empty name raises an error
        with self.assertRaises(Exception):
            Project.objects.create(name="")

    def test_project_creation_with_long_name(self):
        # Test that creating a project with a name that exceeds the max length raises an error
        long_name = "A" * 256  # Assuming max_length is 255
        with self.assertRaises(Exception):
            Project.objects.create(name=long_name)

    def test_project_creation_with_special_characters(self):
        # Test that creating a project with special characters in the name works
        project = Project.objects.create(name="Project @123-_")
        assert project.id is not None
        assert project.name == "Project @123"
    
    def test_project_creation_with_duplicate_name(self):    
        # Test that creating a project with a duplicate name raises an error
        Project.objects.create(name="Duplicate Project")
        with self.assertRaises(Exception):
            Project.objects.create(name="Duplicate Project")
        
    def test_project_creation_with_whitespace_name(self):
        # Test that creating a project with a name that is only whitespace raises an error
        with self.assertRaises(Exception):
            Project.objects.create(name="   ")