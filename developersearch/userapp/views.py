from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from . models import profile
from .forms import CustomForm
from django.contrib import messages
def userprofile(request):
    allprofiles=profile.objects.all()
    return render(request,'userapp/userprofile.html',{ 'profiles':allprofiles})



@login_required(login_url="login")
def profilevisit(request,pk):
    userProfile=profile.objects.get(id=pk)
    skillset=userProfile.skills_set.all
    projectset=userProfile.manageproject_set.all
    return render(request,'userapp/profilevisit.html',{'userProfile':userProfile,'skillset':skillset,'projectset':projectset})




def loginpage(request):
    context = {'page': 'login'}

    if request.user.is_authenticated:
        return redirect('userprofile')

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User doesn't exist")
            return redirect('login')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            print("LOgin DOne")
            login(request,user)
            return redirect('userprofile')

        else:
            messages.error(request,"Username or password is incorrect ")




    return render(request,'userapp/loginregister.html',context)



def logoutpage(request):
    logout(request)
    messages.success(request, " User account logout successfully ")
    return redirect('login')



def registeruser(request):
    form=CustomForm()
    context = {'page': 'register','form':form}
    if request.method=='POST':
        form=CustomForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request," User account created ")
            login(request, user)
            return redirect('userprofile')
        else:
            messages.error(request,"An unwanted error occured")


    return render(request,'userapp/loginregister.html',context)



