from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer, MessageSerializer
from projects.models import Project
from folio.models import ContactMessage
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

class ProductViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get_serializer_context(self):
        return {"request": self.request}
    
    def delete(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        if project is not None:
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT  )
    

class MessageViewSet(ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = MessageSerializer
    
    def get_serializer_context(self):
        return{"request": self.request }
    
    def delete(self, request, pk):
        message = get_object_or_404(ContactMessage, pk=pk)
        if message is not None:
            return Response({"message": "mesazhi nuk fshihet"},  status=status.HTTP_405_METHOD_NOT_ALLOWED)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        




