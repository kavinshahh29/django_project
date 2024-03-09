import uuid
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=250,blank=True,null=True)
    username=models.CharField(max_length=250,blank=True,null=True)
    
    email=models.EmailField(max_length=500,blank=True,null=True)
    About=models.CharField(max_length=500,blank=True,null=True)
    Bio=models.TextField(blank=True,null=True)
    X_link=models.CharField(null=True,blank=True,max_length=500)
    Instagram_link=models.CharField(null=True,blank=True,max_length=500)
    Profile_img=models.ImageField(null=True,blank=True,upload_to='Profiles/',default='Profiles/OIP.jpg')
    Github_link=models.CharField(null=True,blank=True,max_length=500)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4,unique=True)


    def __str__(self):
        return str(self.user.username)
 



