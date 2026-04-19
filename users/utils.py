from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchProfiles(request):
    search_query = request.GET.get('search_query') if request.GET.get('search_query') != None else ''
    skills = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) | 
        Q(skill__in=skills)).distinct()
    return profiles, search_query

def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    if page is None:
        page = 1
    paginator = Paginator(profiles, results)
    try:
        profiles = paginator.get_page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.get_page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.get_page(paginator.num_pages)
    title = "Profiles"

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1
    right_index = int(page) + 5
    if right_index > profiles.paginator.num_pages:
        right_index = profiles.paginator.num_pages + 1
    custom_range = range(left_index, right_index)
    return profiles, custom_range