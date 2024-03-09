from django.contrib import admin

# Register your models here.

from .models import ManageProject,Project_Review,Tag

admin.site.register(ManageProject)
admin.site.register(Project_Review)
admin.site.register(Tag)




