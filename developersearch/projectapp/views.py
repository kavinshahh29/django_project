from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ProjectForm
from .models import ManageProject
from django.contrib.auth.decorators import login_required
def projectdisplay(request,pk):
   context = ManageProject.objects.filter(id=pk).first()
   print(context)
   print(context.description)
   if context is None:
        # Handle case where object with given PK does not exist
      return HttpResponse("Object not found", status=404)
   return render(request,'projectapp/single_project.html',{'ff':context})

# def single_project(request):
#     return render(request,'projectapp/single_project.html')

@login_required(login_url="login")
def CreateProject(request):
    form = ProjectForm()
    if request.method=='POST':
      print(request.POST)
      form = ProjectForm(request.POST,request.FILES)
      if form.is_valid():

          form.save()
          return redirect('projects')

    context={'form':form}
    return render(request,'projectapp/project_form.html',context)


def projects(request):
    form = ManageProject.objects.all()  # Use lowercase 'objects' here
    context = {'form': form}
    return render(request, 'projectapp/projects.html', context)



@login_required(login_url="login")
def UpdateProject(request,pk):
    Project=ManageProject.objects.get(id=pk)
    form = ProjectForm(instance=Project)
    if request.method=='POST':
      print(request.POST)
      form = ProjectForm(request.POST,request.FILES,instance=Project)
      if form.is_valid():

          form.save()
          return redirect('projects')

    context={'form':form}
    return render(request,'projectapp/project_form.html',context)

@login_required(login_url="login")
def DeleteProject(request,pk):
    project=ManageProject.objects.get(id=pk)
    context = {'form': project}
    if request.method=='POST':

        project.delete()
        return redirect('projects')
    return render(request,'projectapp/delete_object.html',context)


