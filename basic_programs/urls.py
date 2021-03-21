from django.urls import path

from . import views

urlpatterns = [
    path("projects",views.projects),
     path("factorial-number",views.codes),
     path("fibonacci-series",views.codes)

]