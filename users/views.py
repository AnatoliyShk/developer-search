from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill
from django.db.models import Q
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, ProfileForm
from .utils import searchProfiles, paginateProfiles

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            user = None

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account created successfully')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles, search_query = searchProfiles(request)
    profiles, custom_range = paginateProfiles(request, profiles, 4)
    context = {'profiles': profiles, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    skills = profile.skill_set.exclude(description__exact="")
    projects = profile.project_set.all()
    return render(request, 'users/user-profile.html', {'profile': profile, 'skills': skills, 'projects': projects})

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    return render(request, 'users/account.html', {'profile': profile})

@login_required(login_url='login')
def editAccount(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('user-account')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/profile_form.html', {'form': form})

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm(request.POST)

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill created successfully')
            return redirect('user-account')

    return render(request, 'users/skill_form.html', {'form': form})

@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(request.POST, instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill updated successfully')
            return redirect('user-account')

    return render(request, 'users/skill_form.html', {'form': form})

def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('user-account')
    return render(request, 'users/delete_template.html', {'object': skill})

@login_required(login_url='login')
def inbox(request):
    context = {}
    return render(request, 'users/inbox.html', context)