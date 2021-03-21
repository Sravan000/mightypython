from django.urls import path

from . import views

urlpatterns = [
    path("projects",views.projects),
     path("testing-11",views.codes),
     path("fibonacci-series",views.codes)

]