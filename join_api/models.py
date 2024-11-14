from django.db import models
 
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bgcolor = models.CharField(max_length=7)
 
    def __str__(self):
        return self.name
    
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()  
    dueDate = models.DateField()      
    priorit = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    subtask = models.JSONField()     
    def __str__(self):
        return self.title
