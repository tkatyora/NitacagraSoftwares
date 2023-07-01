from django.db.models.signals import post_save
from .models import *
from . import views
from django.dispatch  import receiver


@receiver(post_save, sender=servicesTable)
def create_detailedDscription(sender,instance,created,*args,**kwargs):
    if created:
        DetailedDisc = Detailed.objects.create(
           service=instance 
        )
        DetailedDisc.save

# creating the instance of the functinality after creating the Detailed explanations
@receiver(post_save, sender=Detailed)
def create_functionality(sender,instance,created,*args,**kwargs):
    if created:
        Func = Functionality.objects.create(
           details= instance
        )
        Func.save
        
        


        
        
#post_save.connect(create_profile, sender=User)  another way of not using the receiver decorator