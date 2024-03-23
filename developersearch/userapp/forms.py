from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from django.contrib.auth.models import User


class CustomForm(UserCreationForm):    # inheriting UserCreationForm
    class Meta:   #editing fields to show
        model = User
        fields = ['first_name','username','email','password1','password2']
        labels={
            'first_name':'Name',
        } #labels will change firstname to name which can be seen on register page
