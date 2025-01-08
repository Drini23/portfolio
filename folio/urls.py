from django .urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
     path('contact/', views.contact_view, name='contact'),
     path('success/', views.contact_success_view, name='success'),
     path('delete/<int:pk>/', views.delete_message, name='delete'),
     path('resume/', views.resume, name="resume"),
]