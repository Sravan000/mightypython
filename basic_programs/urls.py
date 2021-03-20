from django.urls import path

from . import views

urlpatterns = [
    path("projects",views.projects),
     path("testing-11",views.codes),
     path("testing-12",views.codes)

]