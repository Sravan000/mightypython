from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import PythonProjectsCode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
# Create your views here.

def home(request):
    return render(request,'index.html')

def index(request):
    return redirect('/')

def contributors(request):
    return render(request,'contributors.html')

def projects(request):
    title = "Python Projects"
    projects = PythonProjectsCode.objects.all()
    paginator = Paginator(projects, 2) # Show 25 contacts per page

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

def codes(request):
    if request.method == 'POST':
            project_name = request.POST.get('project_name')
            print('project name: ',project_name)

            code = PythonProjectsCode.objects.get(project_link=project_name)
            projects = PythonProjectsCode.objects.all()
            randomlist = random.sample(range(0, len(projects)), 4)

            related_projects = [projects[i] for i in randomlist]
            print(related_projects)
            random.seed(10)
            is_output_image = False
            if code.python_output == "":
                is_output_image = True
            return render(request,"projects_base_code.html",{"code":code,"is_output_image":is_output_image,"related_projects":related_projects})
