from django.shortcuts import render
from .models import Email
from .serializers import EmailSerializer
from rest_framework import generics, permissions,status
from rest_framework.response import Response

# Create your views here.

class PostEmails(generics.CreateAPIView):
    queryset=Email.objects.all()
    serializer_class=EmailSerializer
    
class ListEmails(generics.ListAPIView):
    queryset=Email.objects.all()
    serializer_class=EmailSerializer
    
