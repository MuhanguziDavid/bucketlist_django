from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """Defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save post data when creating a new bucketlist."""
        serializer.save()
