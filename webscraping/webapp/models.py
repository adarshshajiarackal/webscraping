from django.db import models

# Create your models here.
class link(models.Model):
    links=models.CharField(max_length=500, blank=True,null=True)
    string=models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):
        return self.string
    