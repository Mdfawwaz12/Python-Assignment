from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)



