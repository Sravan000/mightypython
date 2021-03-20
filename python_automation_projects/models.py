from django.db import models

# Create your models here.
class PythonAutomationProjectsCode(models.Model):
    profile_image = models.ImageField(upload_to = 'pics',blank=True, null=True)
    project_name  = models.CharField(max_length = 100)
    contributor_name = models.CharField(max_length = 100,blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    project_description = models.TextField()
    project_link = models.CharField(max_length = 100)
    myfile = models.FileField(blank=True, null=True)
    python_code = models.TextField()
    output_image = models.ImageField(upload_to = 'pics',blank=True, null=True)
    python_output = models.TextField(blank=True, null=True)
    project_visibility = models.BooleanField(default = False)
    dificulty_level = models.IntegerField(blank=True, null=True)