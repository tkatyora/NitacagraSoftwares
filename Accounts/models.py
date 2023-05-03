from django.db import models
from django.contrib.auth.models import User,AbstractUser


# NOTES
# 1.content creater are Customers and blog writers
# 2.create a role class in the portal application that have that roles 
# 3.nitacagraName is customer . content creater or murimiwangu
# 4.all tables people should be here
# class User(AbstractUser):
#     is_nitacagra = models.BooleanField(default=False , null=True)
#     is_customer= models.BooleanField(default=True,null=True)
class NitacagraUsers(models.Model):
        Gender = [('male','Male'),('female','Female')]
        nitacagraName =[('customer','customer'),
                        ('admin','Admin'),
                        ('creater','contentCreater')]
        phoneNumber = models.CharField(max_length=100,null=True)
        city = models.CharField(max_length=100,null=True)
        address = models.CharField(max_length=50, null= True,blank=True) 
        profilePicture = models.ImageField(upload_to ='Pictures', blank=True ,null= True) 
        nitacagraName = models.CharField(max_length=50,null = True,blank=True, choices=nitacagraName)
        gender = models.CharField( max_length=50 , choices = Gender)
        personalInfo = models.OneToOneField(User, verbose_name="Personal Infomation", on_delete=models.CASCADE,null=True)
        
        def __str__(self):
            return f"Information for : {self.personalInfo} "

class ContentCreater(models.Model):
    user = models.OneToOneField("NitacagraUsers", on_delete=models.CASCADE ,null =True)
    companyNumber =models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return f"customer Name : {self.user.username}"
       
class StaffTable(models.Model):
    user = models.OneToOneField("NitacagraUsers", on_delete=models.CASCADE ,null =True)
    Companycode =models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return f"customer Name : {self.user.username}"

class customers(models.Model):
    account =[('Yes','Create an Account'),
              ('No','Do Not Create an Account')]
    user = models.OneToOneField("NitacagraUsers", on_delete=models.CASCADE ,null =True)
    Account = models.CharField(choices = account , null = True,max_length=20)
    
    def __str__(self):
        return f' information of ==> {self.FullName} ' 
  
