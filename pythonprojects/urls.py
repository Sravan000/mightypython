from django.urls import path

from . import views

urlpatterns = [
    path("",views.home, name = "home"),
    path("contributors",views.contributors, name = "contributors"),
    path("home",views.index, name = "home"),
    path("projects",views.projects),
    path("checking-link",views.codes),
    path("checking-1",views.codes),
    path("checking-2",views.codes)

]