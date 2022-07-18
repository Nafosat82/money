from django.urls import re_path,path
from .views import UserRegisterSerializer
from rest_framework import routers
from .views import UserRegisterView, CategoryViewset

router = routers.SimpleRouter()
router.register(r'category', CategoryViewset)

urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
]+router.urls
