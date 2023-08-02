from django.urls import path
from resume.views import HomeView , ExperienceView , EducationView , SkillsView , ProjectsView , addProjectView 
# from resume.views projects_view



app_name = "resume"

urlpatterns = [

    path('', HomeView.as_view(), name = 'home'),
    path('experience/', ExperienceView.as_view(), name = 'experience'),
    path('projects/', ProjectsView.as_view(), name = 'projects'),
    path('add_project/', addProjectView.as_view(), name = 'add_project' ),
    path('skills/', SkillsView.as_view(), name = 'skills'),
    path('education/', EducationView.as_view(), name = 'education'),
    # path('addProject/', projects_view, name = 'addProject'),
    
]

