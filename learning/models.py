from django.db import models

# Create your models here.
class TrialProject(models.Model):
    category = models.CharField(max_length=25 )
    name= models.CharField(max_length=25 )
    pic = models.ImageField(upload_to ='pics',null = True, blank = True)
    
    def  __str__(self):
        return self.name
