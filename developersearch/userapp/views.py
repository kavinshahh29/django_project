from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import profile, Skills, Message
from .forms import CustomForm, ProfileEditform, Skillform,Msgform
from django.contrib import messages
def userprofile(request):
    allprofiles=profile.objects.all()

    return render(request,  'userapp/userprofile.html',{'profiles':allprofiles})


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
            return redirect('editprofile')
        else:
            messages.error(request,"An unwanted error occured")


    return render(request,'userapp/loginregister.html',context)





@login_required(login_url='login')
def ownprofile(request):
    profile=request.user.profile
    skillset = profile.skills_set.all
    projectset = profile.manageproject_set.all
    context={'profile':profile,'skillset':skillset,'projectset':projectset}

    return render(request,'userapp/ownprofile.html',context)

@login_required(login_url='login')
def editprofile(request):
    profile=request.user.profile
    profileform=ProfileEditform(instance=profile)
    if request.method=='POST':
        form=ProfileEditform(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('ownprofile')


    context={'profileform':profileform}
    return render(request,'userapp/profile_edit.html',context)



@login_required(login_url='login')
def addSkill(request):
    profile=request.user.profile
    form=Skillform()
    if request.method=='POST':
        form=Skillform(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.owner=profile
            skill.save()
            return redirect('ownprofile')

    context={'form':form}
    return render(request,'userapp/skilledit.html',context)



@login_required(login_url='login')
def searchdeveloper(request):
    searchquery = ''
    if request.GET.get('query'):
        searchquery = request.GET.get('query')
        skillsquery = Skills.objects.filter(name__icontains=searchquery)
        allprofiles = profile.objects.distinct().filter(
            Q(name__icontains=searchquery) | Q(skills__in=skillsquery)
        )
        return render(request, 'userapp/userprofilesearch.html', {'profiles': allprofiles})
    else:
        allprofiles = profile.objects.all()
        return render(request, 'userapp/userprofile.html', {'profiles': allprofiles})



@login_required(login_url='login')
def msg(request):
    user_profile = request.user.profile
    unread=Message.objects.filter(Q(recipient=user_profile,read=False))
    allmessages = Message.objects.filter(Q(recipient=user_profile))

    return render(request, 'userapp/inbox.html', {'allmessages': allmessages,'unread':unread})


@login_required(login_url='login')
def viewmsg(request, pk):



    msg = Message.objects.get(id=pk)
    if  msg.read==False:
        msg.read = True
        msg.save()

    return render(request, 'userapp/message.html', {'msg': msg})


@login_required(login_url='login')
def sendmsg(request,pk):
    form=Msgform()
    recipient=profile.objects.get(id=pk)

    sender=request.user.profile

    if request.method=='POST':
        form=Msgform(request.POST)
        if form.is_valid():
            msg=form.save(commit=False)
            msg.sender=sender
            msg.recipient=recipient
            msg.save()
            messages.success(request, "Message successfully delivered")
            return redirect('profilevisit',pk=recipient.id)

    return render(request,'userapp/message_form.html',{'recipient':recipient,'form':form})