from django.shortcuts import render
from .models import PythonSoftwares
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def show_projects(request):
    title = "Sofwares Developed using Python"
    projects = PythonSoftwares.objects.all()
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

    return render(request,'softwares.html',{'title':title,'projects':projects})


def show_software(request):
    if request.method == 'POST':
            project_name = request.POST.get('project_name')
            print('project name: ',project_name)

            code = PythonSoftwares.objects.get(project_link=project_name)
            projects = PythonSoftwares.objects.all()
            
            return render(request,"software_using_python.html",{"software":code})
