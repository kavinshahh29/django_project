from django.db import models

import uuid

from userapp.models import profile

class ManageProject(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    featured_img=models.ImageField(null=True, blank=True,default='images/default.jpg')
    demo_link=models.CharField(max_length=2500,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,unique=True)
    tag=models.ManyToManyField('Tag',blank=True)
    reacts=models.IntegerField(default=0,null=True,blank=True)
    ratio=models.IntegerField(default=0,null=True,blank=True)
    projectowner=models.ForeignKey(profile,on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return self.title

class Project_Review(models.Model):
     project=models.ForeignKey(ManageProject,on_delete=models.CASCADE)
     body=models.CharField(max_length=200,null=True,blank=True)
     id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,unique=True)
     created=models.DateTimeField(auto_now_add=True)
     selectchoice={
         ('Like','Liked Post'),
         ('Unlike','Unliked Post'),
     }
     value=models.CharField(max_length=200,choices=selectchoice)
     id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,unique=True)
     

     def __str__(self):
         return self.value


class Tag(models.Model):

    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name




