from django.urls import path
from projects import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path('certeficate/', views.certificate, name='certeficate'),
    path('certification_detail/<int:pk>', views.certification_detail, name="certification_detail")
]