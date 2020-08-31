from django.shortcuts import render
from .models import Blogger
from .serializers import BloggerSerializer
from rest_framework import routers, serializers, viewsets
# Create your views here.
class BloggerViewSet(viewsets.ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer