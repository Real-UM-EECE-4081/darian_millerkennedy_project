from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField(null=True, default=0.0)
    description = models.TextField(default='')

    def __str__(self):
	    return self.name