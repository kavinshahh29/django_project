from django.shortcuts import render

from projectapp.models import ManageProject
# Create your views here.
from . models import profile

def userprofile(request):
    allprofiles=profile.objects.all()
    return render(request,'userapp/userprofile.html',{ 'profiles':allprofiles})



def profilevisit(request,pk):
    userProfile=profile.objects.get(id=pk)
    skillset=userProfile.skills_set.all
    projectset=userProfile.manageproject_set.all
    return render(request,'userapp/profilevisit.html',{'userProfile':userProfile,'skillset':skillset,'projectset':projectset})

