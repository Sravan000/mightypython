from django.shortcuts import render
from .models import PythonAutomationProjectsCode
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
# Create your views here.
def projects(request):
    title = "Python Automation Projects"
    projects = PythonAutomationProjectsCode.objects.all()
    paginator = Paginator(projects, 10) # Show 25 contacts per page

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

            code = PythonAutomationProjectsCode.objects.get(project_link=project_name)
            projects = PythonAutomationProjectsCode.objects.all()
            randomlist = random.sample(range(0, len(projects)), 1)

            related_projects = [projects[i] for i in randomlist]
            print(related_projects)
            random.seed(10)
            is_output_image = False
            if code.python_output == "":
                is_output_image = True
            return render(request,"projects_base_code.html",{"code":code,"is_output_image":is_output_image,"related_projects":related_projects})
