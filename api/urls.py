from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
from django.urls import include

router =  DefaultRouter()
router.register('project', views.ProductViewSet)
router.register('message', views.MessageViewSet)
router.urls

urlpatterns = [
    path('', include(router.urls)),
   
]