from typing import Any
from django import http
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView , FormView
from resume.models import Project
from resume.forms import ProjectForm


class HomeView(TemplateView):
    template_name = "index.html"

class ExperienceView(TemplateView):
    template_name = "experience.html" 

class EducationView(TemplateView):
    template_name = "education.html"

class SkillsView(TemplateView):
    template_name = "skills.html"  

class ProjectsView(TemplateView):
    template_name = "projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all().order_by('-id')
        # projects = Project.objects.all().order_by('-id')
        # for i in Project.objects.all().order_by('-id'):
        #     print("****")
        #     print(i.SourceCode)
        # print(context)
        return context
        # return render(self.request, self.template_name, {"projects":projects})
    

class addProjectView(FormView):
    template_name = "add_project.html"  
    form_class = ProjectForm  
    success_url = '/projects/'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object =Project.objects.create (
        Title=form.cleaned_data['title'],
        Text=form.cleaned_data['text'],
        Image=form.cleaned_data['image'],
        SourceCode = form.cleaned_data['sourcecode'],
        Demo =form.cleaned_data['demo']
        )
        
        # messages.add_message(self.request, messages.SUCCESS, 'Project was succesfully added')
        messages.success(self.request, "Project Was Successfully Added", fail_silently=True)
        
        return super().form_valid(form)

# def projects_view(request):
#     # Assuming you have some data to pass to the template
#     project_data = Project.objects.all()
#         # Add more data as needed
    

#     # Pass the data to the template and render the template
#     return render(request, 'projects.html', project_data)

