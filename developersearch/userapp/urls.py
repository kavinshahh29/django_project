from django.urls import path
from . import views


urlpatterns=[
path('loginpage/',views.loginpage,name='login'),
path('loginregister',views.registeruser,name='registeruser'),
path('logoutpage/',views.logoutpage,name='logout'),
path('',views.userprofile,name='userprofile'),
path('profile/<str:pk>/',views.profilevisit,name='profilevisit'),
path('ownprofile/',views.ownprofile,name='ownprofile'),
path('profileedit/',views.editprofile,name='editprofile'),
path('skilladd/',views.addSkill,name='skilladd'),
path('userprofilesearch/',views.searchdeveloper,name='searchdev'),
]



