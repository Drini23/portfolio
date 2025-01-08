from django.db import models

# Create your models here.



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class Resume(models.Model):
    title = models.CharField(max_length=200)
    image = models.FileField(upload_to="certificate_resume/", blank=True)


    def __str__(self):
        return self.title