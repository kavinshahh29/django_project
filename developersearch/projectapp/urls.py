
from django.urls import path
from . import views

urlpatterns=[
    path('projectd/<str:pk>/', views.projectdisplay, name='projectd'),
    path('create-project/',views.CreateProject,name='create-project'),
    # path('',views.single_project,name='single_project'),
    path('',views.projects,name='projects'),
    path('update-project/<str:pk>/',views.UpdateProject,name='updateproject'),
    path('delete-project/<str:pk>/',views.DeleteProject,name='deleteproject'),

]