from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import ContactForm
from .models import ContactMessage, Resume
from projects.models import Project, Certificate
from django.core.mail import send_mail, mail_admins, BadHeaderError



# Create your views here.

def home(request):

    projects = Project.objects.all()
    certificate = Certificate.objects.all()
    resume = Resume.objects.all()
    
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            

            # Create a new ContactMessage instance and save it
            contact_message = ContactMessage.objects.create(
                name=name, email=email, subject=subject, message=message
            )
            contact_message.save()
            return render(request, 'folio/success.html')
    else:
        form = ContactForm()
    
    context = {'form': form, "projects": projects, "certificate": certificate, "resume": resume}
    return render(request, 'folio/home.html', context )


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            

            # Create a new ContactMessage instance and save it
            contact_message = ContactMessage.objects.create(
                name=name, email=email, subject=subject, message=message
            )
            contact_message.save()
            return redirect('folio/success.html')
    else:
        form = ContactForm()

    return render(request, 'folio/contact.html', {'form': form})

def delete_message(request, pk):
    message = ContactMessage.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('/')
    context = {"message": message}
    return render(request, 'folio/delete.html', context)
    

  
def contact_success_view(request):
    messages = ContactMessage.objects.all()
    context = {"messages": messages}
    return render(request, 'folio/message.html', context)



def resume(request):
    resume = Resume.objects.all()
    context = {"resume": resume}
    return render(request, "folio/resume.html", context)



