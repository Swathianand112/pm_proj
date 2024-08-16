from django.contrib import admin

# Register your models here.

from .models import Employee, Project, ProjectAssignment

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(ProjectAssignment)
