from rest_framework import serializers
from .models import MyModel, Contacts

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        contact = Contacts
        fields = '__all__'
