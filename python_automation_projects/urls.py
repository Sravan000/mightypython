from django.urls import path

from . import views

urlpatterns = [
    path("projects",views.projects),
    path("checking-5",views.codes),


]