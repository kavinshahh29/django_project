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









# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=150)
#     email = models.EmailField(unique= True)
#     first_name = models.CharField(max_length = 100)
#     last_name = models.CharField(max_length = 100)

#     def _str_(self):
#         return self.first_name

# class Profile(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     name = models.CharField(max_length=150)
#     email = models.EmailField()
#     username = models.CharField(max_length=150)
#     bio = models.TextField(blank=True, null=True)
#     profile_image = models.ImageField(null=True, blank=True)
#     social_github = models.URLField(max_length=200, blank=True, null=True)
#     social_twitter = models.URLField(max_length=200, blank=True, null=True)
#     social_linkedin = models.URLField(max_length=200, blank=True, null=True)

#     def _str_(self):
#         return self.name

# class Message(models.Model):
#     msg_id = models.AutoField(primary_key=True)
#     sender=models.ForeignKey(User,related_name='send_message',on_delete=models.CASCADE,default=None)
#     reciever = models.ForeignKey(User, related_name='recieve_message', on_delete=models.CASCADE,default=None)
#     # name = models.CharField(max_length=150)
#     # email = models.EmailField()
#     subject = models.CharField(max_length=255,blank=True,null=True)
#     body = models.TextField()
#     is_read = models.BooleanField(default=False)

#     def _str_(self):
#         return self.subject

# class Project(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     featured_image = models.ImageField(null=True, blank=True)
#     tags = models.CharField(max_length=200)

#     def _str_(self):
#         return self.title

# class Skill(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     proficiency_level = models.CharField(max_length=50)

#     def _str_(self):
#         return self.name