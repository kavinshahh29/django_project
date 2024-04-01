from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from django.contrib.auth.models import User

from userapp.models import profile, Skills


class CustomForm(UserCreationForm):    # inheriting UserCreationForm
    class Meta:   #editing fields to show
        model = User
        fields = ['first_name','username','email','password1','password2']
        labels={
            'first_name':'Name',
        } #labels will change firstname to name which can be seen on register page


class ProfileEditform(ModelForm):
    class Meta:
        model=profile
        fields=['name','username','email','About','Bio','X_link','Instagram_link','Profile_img','Github_link']




class Skillform(ModelForm):
    class Meta:
        model=Skills
        fields=['name','desc']



