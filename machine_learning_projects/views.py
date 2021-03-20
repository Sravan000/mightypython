from django.shortcuts import render
from .models import MachineLearningProjects
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.clickjacking import xframe_options_exempt

import random


# Create your views here.
def projects(request):
    title = "Machine Learning Projects"
    projects = MachineLearningProjects.objects.all()
    paginator = Paginator(projects, 1) # Show 25 contacts per page

    page = request.GET.get('page',1)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        projects = paginator.page(paginator.num_pages)

    return render(request,'projects_menu.html',{'title':title,'projects':projects})



@xframe_options_exempt
def codes(request):
    if request.method == 'POST':

        project_name = request.POST.get('project_name')
        print('project name: ',project_name)

        code = MachineLearningProjects.objects.get(project_link=project_name)
        projects = MachineLearningProjects.objects.all()
        random.seed(10)
        randomlist = random.sample(range(0, len(projects)), 1)

        related_projects = [projects[i] for i in randomlist]
        print(related_projects)
            
        return render(request,"machine_learning.html",{"code":code,"related_projects":related_projects})

    