from rest_framework import generics
from .models import Contact, Task
from .serializers import ContactSerializer, TaskSerializer

from rest_framework.response import Response
from rest_framework import status

# handle contacts...

class ContactcreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDeleteView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# handle created tasks...

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
