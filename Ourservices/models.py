from django.db import models
from Accounts.models import customers

#Create your models here.

class servicesTable(models.Model):
    sections = [('web','Web Developmnent'),
                ('desktop', 'Desktop Development'),
                ('mobile' ,'Mobile Development'),
                ('network','Networking')]
    section = models.CharField(max_length=20,null=True, choices = sections)
    name = models.CharField(max_length=20,null=True)
    pic = models.ImageField(upload_to ='pics', blank=True ,null= True)
    briefDisc = models.TextField(max_length= 90,null=True)
    FullDisc = models.TextField(max_length=160,null=True)
    oldPrice = models.DecimalField(max_digits=7, decimal_places=2 ,blank=True, null=True)
    newPrice = models.DecimalField(max_digits=7, decimal_places=2 ,null=True)
    specialOffer = models.BooleanField(default=False , null= True)
    created_on =models.DateTimeField( auto_now=False, auto_now_add=True ,null=True)
    updated_on =models.DateTimeField( auto_now=True, auto_now_add=False ,null=True)
    
    
    class Meta:
        ordering = ('-created_on',)
    def __str__(self):
        return f'{self.section } ==> {self.name}' 
    
    
 # order table
class order(models.Model):
    customer = models.ForeignKey(customers, on_delete = models.CASCADE, null = True)
    serviceTable = models.ForeignKey(servicesTable, on_delete = models.CASCADE , null = True)
    orderNumber = models.IntegerField(null=True)
    ReceiveDate = models.DateTimeField( blank = True , null=True)
    SubmitDate = models.DateTimeField(null=True,auto_now_add= True)
    
    def __str__(self):
        return f'order number {self.orderNumber} for  {self.customer.FullName}' 

 
#creating models for our ofered dervices
#first category the services models   


    