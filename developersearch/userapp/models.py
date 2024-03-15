import uuid
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=250,blank=True,null=True)
    username=models.CharField(max_length=250,blank=True,null=True)
    
    email=models.EmailField(max_length=500,blank=True,null=True)
    About=models.CharField(max_length=500,blank=True,null=True,default=" ")
    Bio=models.TextField(blank=True,null=True)
    X_link=models.CharField(null=True,blank=True,max_length=500)
    Instagram_link=models.CharField(null=True,blank=True,max_length=500)
    Profile_img=models.ImageField(null=True,blank=True,upload_to='Profiles/',default='Profiles/OIP.jpg')
    Github_link=models.CharField(null=True,blank=True,max_length=500)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,unique=True)


    def __str__(self):
        return str(self.user.username)
 



class Skills(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(profile,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    desc=models.TextField()


    def __str__(self):
        return str(self.name)



def profiledelete(sender,instance,**kwargs):
    user=instance.user
    user.delete()



def profileCreates(sender,instance,created,**kwargs):
    if created:
        user=instance
        profilecreate=profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

post_save.connect(profileCreates,sender=User)
post_delete.connect(profiledelete,sender=profile)


