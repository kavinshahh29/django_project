from django.urls import path
from . import views


urlpatterns=[

path('',views.userprofile,name='userprofile'),
path('profile/<str:pk>/',views.profilevisit,name='profilevisit'),

]



