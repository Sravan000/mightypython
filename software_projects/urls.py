from django.urls import path

from . import views

urlpatterns = [
    path("projects",views.show_projects),
    path("checking-6",views.show_software)

]