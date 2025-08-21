from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PaperViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('paper', PaperViewSet)
router.register('user', UserViewSet)
urlpatterns = [
    path('', include(router.urls))
]