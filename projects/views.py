from django.shortcuts import render, get_object_or_404
from projects.models import Project, Certificate


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/detail.html", context)

def certificate(request):
    certificate = Certificate.objects.all()
    context = {'certificate': certificate}
    return render(request, 'projects/certificate.html', context )


def certification_detail(request, pk):
    certification = get_object_or_404(Certificate, pk=pk)
    context = {'certification': certification}
    return render(request, 'projects/certification_detail.html', context)