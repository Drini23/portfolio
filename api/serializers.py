from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from projects.models import Project
from folio.models import ContactMessage


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
        
class MessageSerializer(ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
    