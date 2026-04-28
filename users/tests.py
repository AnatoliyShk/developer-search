from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

def test_user_creation():
    # Test that a user can be created successfully
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    assert user.id is not None
    assert user.username == "testuser"

def test_user_str_representation():
    # Test the string representation of a user
    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    assert str(user) == "testuser"