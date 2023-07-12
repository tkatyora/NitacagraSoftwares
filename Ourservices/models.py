from django.db import models
from django.utils.translation import gettext_lazy as _
from Accounts.models import CustomerWithoutAccount

#Create your models here.
class Detailed(models.Model):
    type = models.CharField(max_length=50 ,default='Custom')# This is the type of the service for example standard , custom in webdev
    Price = models.DecimalField(max_digits=7, decimal_places=2,default=50.00 )
    specialOffer = models.BooleanField(default=False , null= True)
    service = models.ForeignKey( "servicesTable",verbose_name=_("services table"), on_delete=models.CASCADE , null = True) #one service can have many detailed Discription
   
   
   
    def __str__(self):
        return  self.type   
                                                    
class servicesTable(models.Model):
    Name = [('web','Web Development'),
            ('blogHost','Free Blog Hosting'),
            ('staticsites','Static Websites')]
    name = models.CharField(max_length=50,null=True ,choices=Name) #This name is the name of the Overal service for example Web development
    picture = models.ImageField(_("Picture"), upload_to='Pictures', height_field=None, width_field=None, max_length=None , null =True ,blank = True)
    Discription = models.TextField(max_length= 150,null=True)
    #DetailedDisc = models.ForeignKey("Detailed", on_delete=models.CASCADE,null =True)
    specialOffer = models.BooleanField(default=False , null= True)
    created_on =models.DateTimeField( auto_now=False, auto_now_add=True ,null=True)
    updated_on =models.DateTimeField( auto_now=True, auto_now_add=False ,null=True)
    
    
    class Meta:
        ordering = ('-created_on',)
        
    def __str__(self):
        return f' Name of Service : ' + self.name 
    
    # this code is to solve problem that are caused due to Imagies Not Found
    @property
    def ImageUrl(self):
        try:
            url = self.picture.url
        except:
             url = ''
             
        return url
            
    
  


class Functionality(models.Model):
    #details = models.OneToOneField("Detailed", on_delete=models.CASCADE)
    Pages = models.CharField(max_length=60 ,null=True)     
    HostPlaform = models.CharField(max_length=50 ,null=True) 
    HostDays = models.CharField(max_length=50 ,null=True) 
    Responsive = models.CharField(max_length=50 ,null=True) 
    SEO = models.BooleanField(default=True)
    SocialMedia = models.CharField(max_length=50 ,null=True) 
    
    def  __str__(self):
        return {self.Pages}
        
 # order table
class order(models.Model):
    orderNumber =models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    customer = models.ForeignKey(CustomerWithoutAccount, on_delete = models.CASCADE, null = True)
    service = models.ForeignKey(servicesTable, on_delete = models.CASCADE , null = True)
    ReceiveDate = models.DateTimeField( blank = True , null=True)
    SubmitDate = models.DateTimeField(null=True,auto_now_add= True)
    
    def __str__(self):
        return f'order number {self.orderNumber} for  {self.customer.FullName}' 




    