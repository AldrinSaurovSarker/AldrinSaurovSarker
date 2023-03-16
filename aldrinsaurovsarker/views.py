from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    profile = get_object_or_404(Profile, id=1)
    name = profile.name.split()

    skillType = {item[0] for item in list(set(Skills.objects.order_by('level').values_list('level')))}
    skills = []
    for skill in skillType:
        skills.append(Skills.objects.order_by('name').filter(level=skill))
    
    providerSet = {item[0] for item in list(set(Certificates.objects.values_list('provider')))}
    certificates = []
    for provider in providerSet:
        certificates.append(Certificates.objects.filter(provider=provider))

    extras = Extras.objects.all()

    experiences = Experiences.objects.all()
    
    educations = Educations.objects.all()
    
    projectSet = {item[0] for item in list(set(Projects.objects.values_list('ptype')))}
    projects = []
    for project in projectSet:
        projects.append(Projects.objects.filter(ptype=project))

    context = {
        'profile':profile,
        'name':name,
        'skills':skills,
        'certificates':certificates,
        'extras':extras,
        'educations':educations,
        'experiences':experiences,
        'projects':projects
        }
    
    return render(request, 'index.html', context)
