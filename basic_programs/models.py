from django.db import models

# Create your models here.
class programs(models.Model):
    program_name = models.CharField(max_length=1000)
    c_code = models.TextField()
    java_code =  models.TextField()
    program_description = models.TextField()
    python_code =  models.TextField()
    output = models.TextField()
    program_link = models.CharField(max_length=1000,null=True)
    program_visibility = models.BooleanField(default = False)