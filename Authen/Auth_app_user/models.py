from django.db import models

# Create your models here.
class Request_details(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=256)
    number=models.CharField(max_length=12)
    status=models.CharField(max_length=25,default="Pending")
    def __str__(self):
        return self.name
    