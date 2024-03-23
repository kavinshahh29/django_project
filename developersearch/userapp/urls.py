from django.urls import path
from . import views


urlpatterns=[
path('loginpage/',views.loginpage,name='login'),
path('loginregister',views.registeruser,name='registeruser'),
path('logoutpage/',views.logoutpage,name='logout'),
path('',views.userprofile,name='userprofile'),
path('profile/<str:pk>/',views.profilevisit,name='profilevisit'),

]



