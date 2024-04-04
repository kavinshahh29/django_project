from django.contrib import admin

# Register your models here.

from .models import ManageProject,Tag

admin.site.register(ManageProject)
admin.site.register(Tag)




