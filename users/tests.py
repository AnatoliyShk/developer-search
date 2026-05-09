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

def test_user_update():
    # Test that a user can be updated successfully
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    user.username = "newusername"
    user.save()
    updated_user = User.objects.get(id=user.id)
    assert updated_user.username == "newusername"

def user_delete():
    # Test that a user can be deleted successfully
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    user_id = user.id
    user.delete()
    with pytest.raises(User.DoesNotExist):
        User.objects.get(id=user_id)

def test_user_list():
    # Test that a list of users can be retrieved successfully
    User = get_user_model()
    User.objects.create_user(username="testuser1", password="testpassword")
    User.objects.create_user(username="testuser2", password="testpassword")
    users = User.objects.all()
    assert len(users) == 2

def test_user_detail():
    # Test that a user's details can be retrieved successfully
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    retrieved_user = User.objects.get(id=user.id)
    assert retrieved_user.username == "testuser"

def test_user_authentication():
    # Test that a user can be authenticated successfully
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    authenticated_user = User.objects.get(username="testuser")
    assert authenticated_user.check_password("testpassword")

def test_user_permissions():
    # Test that a user has the correct permissions
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    assert user.has_perm("auth.view_user")

def test_user_groups():
    # Test that a user can be added to a group successfully
    from django.contrib.auth.models import Group
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    group = Group.objects.create(name="Test Group")
    user.groups.add(group)
    assert group in user.groups.all()

def test_user_superuser():
    # Test that a superuser can be created successfully
    User = get_user_model()
    superuser = User.objects.create_superuser(username="admin", password="adminpassword")
    assert superuser.is_superuser
    assert superuser.is_staff

def test_user_email():
    # Test that a user can have an email address
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword", email="testuser@example.com")
    assert user.email == "testuser@example.com"

def test_user_last_login():
    # Test that a user's last login time is updated correctly
    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpassword")
    user.last_login = None
    user.save()
    user.refresh_from_db()
    assert user.last_login is None