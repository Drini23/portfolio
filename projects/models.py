from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=255)
    image = models.FileField(upload_to="project_images/", blank=True)
    github_url = models.URLField(max_length=200, blank=True)
    live_hots = models.URLField(max_length=200, blank=True)
    

    def __str__(self):
        return self.title
    
    
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    compani = models.CharField(max_length=200)
    image = models.FileField(upload_to="certificate_images/", blank=True)
    
    
    def __str__(self):
        return self.title
    
    
