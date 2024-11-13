from django.db import models

class MyModel(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.key


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name 