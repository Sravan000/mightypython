# Generated by Django 3.1.5 on 2021-02-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PythonProjectsCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('project_name', models.CharField(max_length=100)),
                ('contributor_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('project_description', models.TextField()),
                ('project_link', models.CharField(max_length=100)),
                ('myfile', models.FileField(blank=True, null=True, upload_to='')),
                ('python_code', models.TextField()),
                ('output_image', models.ImageField(blank=True, null=True, upload_to='pics')),
                ('python_output', models.TextField(blank=True, null=True)),
                ('project_visibility', models.BooleanField(default=False)),
                ('dificulty_level', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
