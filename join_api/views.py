from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import MyModel, Contacts
from .serializers import ContactsSerializer, MyModelSerializer
from rest_framework import generics
from rest_framework import viewsets

@csrf_exempt
@api_view(['POST'])
def save_item(request):
    serializer = MyModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'errors': serializer.errors})

@api_view(['GET'])
def get_item(request, key):
    try:
        item = MyModel.objects.get(key=key)
        return JsonResponse({'status': 'success', 'data': MyModelSerializer(item).data})
    except MyModel.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Item not found'})
    

class ContactsViewSet(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer