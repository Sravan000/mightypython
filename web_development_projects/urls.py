from django.urls import path

from . import views

urlpatterns = [
   path("projects",views.projects),
    path("testing-10",views.codes)

]