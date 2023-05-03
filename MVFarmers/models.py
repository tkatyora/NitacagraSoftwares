from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Problems(models.Model):
    Priority=[('High','High Priority'),('Medium' , 'Medium Priority'),('Low' ,'Low Priority')]
    #Where body is the discription and symptoms
    body = models.TextField(null= True)
    animal = models.ManyToManyField('animals' ) 
    creater = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    Solution = models.ManyToManyField('Solutions')
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    #this shows the qauntity that is affected 
    numberAffected = models.IntegerField(null=True)
    priority = models.CharField( max_length=50 , choices = Priority ,null=True)
    
    class Meta:
        ordering = ('-created_on')
           
    class Meta:
        verbose_name = ("Farmers Problem")
        verbose_name_plural = ("Farmers Problems")

    def __str__(self):
        return f'Problem created by {self.creater}'

class animals(models.Model):
    Animals=[('chicken', 'Chickens'),]
    name = models.CharField( max_length=80, choices= Animals ,null=True)
    def __str__(self):
        return f'Animal Name {self.name}'
    
    
class Solutions(models.Model):
    
    body = models.TextField(null= True)
   
    def __str__(self):
        return f'Solutions for  {self.body}'


    