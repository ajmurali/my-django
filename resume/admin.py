from django.contrib import admin
from resume.models import Project

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project,ProjectAdmin)
