

from django.forms import ModelForm
from django import forms

from .models import ManageProject

class ProjectForm(ModelForm):
    class Meta:
        model=ManageProject
        fields=['title','description','featured_img','demo_link','tag']

        widgets={
            'tag':forms.CheckboxSelectMultiple()
        }

        def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)

            self.fields['title'].widget.attrs.update(
                {
                    'class':'input',
                    'placeholder':'Enter the title'
                }
            )


            self.fields['description'].widget.attrs.update(
                {
                    'class':'input',
                    'placeholder':'Enter the description'
                }
            )


            self.fields['demo_link'].widget.attrs.update(
                {
                    'class':'input',
                    'placeholder':'Enter The Demo Link'
                }
            )


            self.fields['tag'].widget.attrs.update(
                {
                    'class':'input',
                
                }
            )

            self.fields['featured_img'].widget.attrs.update(
                {
                    'class':'input',
                
                }
            )




