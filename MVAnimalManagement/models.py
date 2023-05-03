# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.
# class fowlRunConditions(models.Model):
#     Temperature = models.IntegerField(null=True)
#     Humidity = models.IntegerField(null=True)
#     Recorded_on = models.DateTimeField( null = True, auto_now_add=True)
#     Update_on = models.DateTimeField( auto_now=True, null= True)
#     System = models.IntegerField(auto_created=True, primary_key=True, verbose_name='MV00',default= '001')
#     Farmer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    
    
#     def __str__(self):
#         return f'Conditions For {self.Farmer}'
    
        