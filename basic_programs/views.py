from django.shortcuts import render
from .models import programs
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
# Create your views here.
def projects(request):
    projects = programs.objects.all()
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

    return render(request,'programs.html',{'projects':projects})

def codes(request):
    if request.method == 'POST':
          project_name = request.POST.get('project_name')
          print('project name: ',project_name)

          code = programs.objects.get(program_link=project_name)
          projects = programs.objects.all()
          random.seed(10)
          randomlist = random.sample(range(0, len(projects)), 2)

          related_projects = [projects[i] for i in randomlist]
          print(related_projects)
            

          return render(request,"beginner_code_display.html",{"code":code,"related_projects":related_projects})
