from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 30)
    community = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
class Chat(models.Model):
    name = models.CharField(max_length = 30)
    message = models.CharField(max_length = 500)
    new = models.CharField(max_length = 5)
