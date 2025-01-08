from django.contrib import admin
from projects.models import Project, Certificate


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Certificate)