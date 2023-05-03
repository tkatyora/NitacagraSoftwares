from django.db import models

# Create your models here.
class advertisment(models.Model):
    Section =[('part1','Carousel/HomeSlide'),
              ('part2','Products and Services'),
              ('services','Offered Services /Slides'),]
    buttons =[('servicebtn','More Services'),
              ('Guidesbtn','  More Projects Guides'),
              ('signUp','Sign Up Today'),
              ('contact','Contact Today'),
              ('learn','Learn More'),]
    section = models.CharField(max_length=20,null=True,choices=Section)
    name = models.CharField(max_length=20,null=True)
    image = models.ImageField(upload_to = 'pics' , blank = True)
    disc = models.TextField(null=True)
    Homebutton = models.CharField(max_length=20, blank = True ,choices=buttons)
    createdOn =models.DateTimeField(null=True, auto_now_add=True)
    Updated = models.DateField(null=True, auto_now=True, auto_now_add=False)
    
    
    
    def __str__(self):
        return f'{self.section} ==> { self.name}'
    
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
   
    