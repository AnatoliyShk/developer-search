from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            user = None

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {'profiles': profiles})

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    return render(request, 'users/user-profile.html', {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills})