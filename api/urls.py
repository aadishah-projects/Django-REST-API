from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.StudentListCreate.as_view() , name= "Student-view-create"),
    path("home/<int:pk>/", views.StudentRetrieveUpdateDestroy.as_view(), name= "Update")
]