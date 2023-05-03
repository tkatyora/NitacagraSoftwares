# from django.db import models
# from diseases.models import Diseases

# # Create your models here.
# class Tips(models.Model):
#     section = [('dis','disease'),('nutr','nutrition'),('phy','physician')]
#     category= models.CharField(max_length=50,null=True ,choices=section)
#     Tip = models.TextField( max_length=200,null=True)
   
#     CreatenOn = models.DateTimeField(null= True,auto_now_add=True)
#     Creater = models.CharField(max_length=50 , null=True)
#     pic = models.ImageField(upload_to ='img',null = True,blank= True)
#     def __str__(self):
#         return f"{self.Disease.name} Tips created by {self.Creater}"
    