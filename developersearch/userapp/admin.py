from django.contrib import admin

# Register your models here.

from .models import profile,Skills,Message

admin.site.register(profile)
admin.site.register(Skills)
admin.site.register(Message)





