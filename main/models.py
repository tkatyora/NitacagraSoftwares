from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class advertisment(models.Model):
    Slides = [('1','One'),('2','Two'),('3','Three')]
    name = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to = 'pics' , blank = True)
    disc = models.TextField(null=True ,blank=True)
    Homebutton = models.CharField(max_length=20, blank = True )
    createdOn =models.DateTimeField(null=True, auto_now_add=True)
    Updated = models.DateField(null=True, auto_now=True, auto_now_add=False)
    slide = models.CharField(_("slide number"), max_length=50, null=True , choices=Slides)

    
    
    def __str__(self):
        return f'Advert for  { self.name}'
    
    
    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
             url = ''
             
        return url
    
class aboutUs(models.Model):
    history =models.TextField(null=True,blank=True)
    visionMision =models.TextField(null=True,blank=True)
    coreValues=models.TextField(null=True,blank=True)
    #management body
    
    takudzwa = models.ImageField(default='default.jpg', upload_to='Pictures', height_field=None, width_field=None, max_length=200,null=True,blank=True)
    gracious = models.ImageField(default='default.jpg' ,upload_to='Pictures', height_field=None, width_field=None, max_length=200,null=True,blank=True)
    carey = models.ImageField(default='default.jpg', upload_to='Pictures', height_field=None, width_field=None, max_length=200,null=True,blank=True)
    nicole = models.ImageField(default='default.jpg', upload_to='Pictures', height_field=None, width_field=None, max_length=200,null=True,blank=True)
    created_on = models.DateTimeField( auto_now_add=True,null=True)
    lastUpadatedOn = models.DateTimeField( auto_now=True, null=True)
    def __str__(self):
        return f'About Us Information last updated on {self.visionMision}'
   
    