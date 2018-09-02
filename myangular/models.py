from django.db import models

# Create your models here.
class cart(models.Model):
    name = models.CharField(max_length = 30)
    price = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

