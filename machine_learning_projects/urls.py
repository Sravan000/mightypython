from django.urls import path

from . import views

urlpatterns = [
     path("projects",views.projects),
     path("checking-7",views.codes),
     path("checking-8",views.codes)

]